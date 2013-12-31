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
--
-- File automatically generated by load_csv_pg.sh
--   changes made here will be lost

CREATE TEMP TABLE polylink_tmp as (
  SELECT cenidl as cenid, polyidl as polyid, tlid
     FROM work.polylink 
     WHERE polyidl > '' and cenidl > ''
  UNION
  -- grab right polyid's when they don't match the left polyid's
  --    otherwise the previous select got them
  SELECT cenidr as cenid, polyidr as polyid, tlid
     FROM work.polylink 
     WHERE polyidr > '' and cenidr > '' and
      not (coalesce(polyidl,'') = polyidr and coalesce(cenidl,'') = cenidr)
);  -- limit to unique records, using UNION (no ALL)

CREATE INDEX polylink_poly_ind on polylink_tmp(polyid,cenid);
CREATE INDEX polylink_tlid_ind on polylink_tmp(tlid);

DROP TABLE if exists gchain_tmp;
CREATE TEMP TABLE gchain_tmp as (
  SELECT DISTINCT g.tlid, p.cenid, p.polyid, g.geom
    FROM
      work.chain g LEFT OUTER JOIN
      polylink_tmp p on (g.tlid = p.tlid)
);


DROP TABLE if exists poly_tmp;
CREATE TEMP TABLE poly_tmp (id serial PRIMARY KEY, geom geometry, cenid text, polyid text);
INSERT INTO poly_tmp (geom, cenid, polyid)
( SELECT St_Polygonize(geom) AS geom, cenid, polyid
 FROM gchain_tmp
 group by cenid, polyid
);
UPDATE poly_tmp set geom = 
   CASE 
    WHEN st_numgeometries(geom) = 1 THEN st_multi(st_geometryn(geom,1))
    ELSE st_multi(st_buffer(geom,0))
   END;


-- CREATE TEMP TABLE poly_tmp (id serial PRIMARY KEY, geom geometry);
-- INSERT INTO poly_tmp (geom)
-- SELECT geom AS geom
-- FROM St_Dump((
--  SELECT St_Polygonize(geom) AS geom
--  FROM work.chain
-- ));

CREATE index poly_tmp__shp__ind on poly_tmp using GIST(geom);
CREATE index polypt__shp__ind on work.polypt using GIST(geom);

DROP table if exists work.poly;
CREATE TABLE work.poly as (
  SELECT pa.*, st_setsrid(g.geom,4269) as geom
    FROM
      work.polyattr pa,
--      work.polypt p,
      poly_tmp g
    WHERE
--      st_intersects(p.geom, g.geom) and
--      pa.cenid = p.cenid and pa.polyid = p.polyid
      pa.cenid = g.cenid and pa.polyid = g.polyid
);

--  CREATE TEMP TABLE poly_xref_tmp as (
--   SELECT id, cenid, polyid FROM work.poly 
--     WHERE id in (SELECT id from work.poly group by 1 having count(*) >1 )
--      or (cenid,polyid) in (SELECT cenid,polyid from work.poly group by 1,2 having count(*) >1 )
--   );
--  CREATE TEMP TABLE poly_dup_tmp as (
--     SELECT id,cenid,polyid FROM poly_xref_tmp 
--       WHERE id in (SELECT id from poly_xref_tmp GROUP BY 1 HAVING count(*) > 1)
--  );
--  DELETE FROM poly_dup_tmp WHERE exists (SELECT 1 FROM poly_xref_tmp x 
--          WHERE poly_dup_tmp.cenid = x.cenid and  
--            poly_dup_tmp.polyid = x.polyid and
--            poly_dup_tmp.id != x.id);
--  DELETE FROM work.poly WHERE (id,cenid,polyid) in (SELECT id,cenid,polyid from poly_dup_tmp);

-- ALTER TABLE work.poly drop id;

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

