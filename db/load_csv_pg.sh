#!/bin/bash

csv=$1

echo "-- TIGER 1992 loader for a County" >ldr.sql

for csv in *.csv; do

tab="work."`basename $csv .csv`

if [ ! -r "$csv" ]; then
  echo "usage: load_csv-pg.sh <csvfile> <pg_Table>"
  exit
fi

if [ -z "$tab" ]; then
  exit
fi

flds=`head -n 1 $csv | sed -e 's/"$/ Text/' -e 's/,/ Text ,/g' -e 's/"/ /g'  `
has_wkt=`echo $flds | grep -c -i wkt`

(
echo "drop table if exists $tab;"
echo "Create Table $tab ( $flds );"
echo "Copy $tab from STDIN  CSV NULL '[';"
awk 'NR>1 { print }' $csv
echo "\."
echo ";" 
if [ $has_wkt -gt 0 ]; then
echo "ALTER TABLE $tab ADD geom geometry;
  UPDATE $tab SET geom = geometryfromtext(wkt,4269) WHERE wkt > '';
  ALTER TABLE $tab drop wkt;

"
fi
) >> ldr.sql

done

st=`head -n 2 Featname.csv | tail -n 1 | cut -c6-7`
(echo "-- post_process.sql

CREATE TEMP TABLE poly_tmp (id serial PRIMARY KEY, the_geom geometry);
INSERT INTO poly_tmp (the_geom)
SELECT geom AS the_geom
FROM St_Dump((
 SELECT St_Polygonize(geom) AS the_geom
 FROM work.chain
));

CREATE index poly_tmp__shp__ind on poly_tmp using GIST(the_geom);
CREATE index polypt__shp__ind on work.polypt using GIST(geom);

DROP table if exists work.poly;
CREATE TABLE work.poly as (
  SELECT pa.*, st_setsrid(g.the_geom,4269) as the_geom, g.id
    FROM
      work.polyattr pa,
      work.polypt p,
      poly_tmp g
    WHERE
      st_intersects(p.geom, g.the_geom) and
      pa.cenid = p.cenid and pa.polyid = p.polyid
);

 CREATE TEMP TABLE poly_xref_tmp as (
  SELECT id, cenid, polyid FROM work.poly 
    WHERE id in (SELECT id from work.poly group by 1 having count(*) >1 )
     or (cenid,polyid) in (SELECT cenid,polyid from work.poly group by 1,2 having count(*) >1 )
  );
 CREATE TEMP TABLE poly_dup_tmp as (
    SELECT id,cenid,polyid FROM poly_xref_tmp 
      WHERE id in (SELECT id from poly_xref_tmp GROUP BY 1 HAVING count(*) > 1)
 );
 DELETE FROM poly_dup_tmp WHERE exists (SELECT 1 FROM poly_xref_tmp x 
         WHERE poly_dup_tmp.cenid = x.cenid and  
           poly_dup_tmp.polyid = x.polyid and
           poly_dup_tmp.id != x.id);
 DELETE FROM work.poly WHERE (id,cenid,polyid) in (SELECT id,cenid,polyid from poly_dup_tmp);

ALTER TABLE work.poly drop id;

  " 
for t in *.csv poly.csv; do
  tab=`basename $t .csv`
  echo "
-- load $tab;
CREATE TABLE if not exists t1992.${tab} ( like work.${tab} );
CREATE TABLE if not exists t1992.${tab}_${st} () inherits (t1992.${tab} );
INSERT INTO t1992.${tab}_${st} ( SELECT * from work.${tab} );
DROP TABLE work.${tab};
"
done
)>post_process.sql


