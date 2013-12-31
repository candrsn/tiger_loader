#!/bin/bash

tgrbase="/home/candrsn/media/CentOS/tiger/tiger_1992/TIGER1992"

echo "
--  DROP SCHEMA t1992 cascade;
  CREATE SCHEMA t1992;
" | psql census

# build a list of already loaded States and Counties
#    polypt a small tuple size, so it should be fastest
echo "SELECT DISTINCT state||county from t1992.polypt ORDER BY 1;" | psql -t -A census > process.list

for st in ${tgrbase}/??; do
  stfp=`basename $st`
  echo "$stfp"

  if [ $stfp -gt "00" ] ; then # act on valid states
    for cty in ${st}/[0-9]*.zip; do
      ctyfp=`basename $cty .zip`
      echo "Scan $ctyfp"

      ptest=`grep -c "$ctyfp" process.list`
      if [ $ptest -eq 0 ]; then 
        # exclude already run counties

        echo "loading data for $ctyfp from $cty"

        rm tmp/* dat/*
        unzip -d tmp $cty
        (
         cd tmp
         sort -T /tmp -t'[' -k1.6,1.15n TGR${ctyfp}.F51 > wrk
         mv wrk TGR${ctyfp}.F51
         sort -T /tmp -t '[' -k1.6,1.15n -k1.16,1.18n TGR${ctyfp}.F52 > wrk
         mv wrk TGR${ctyfp}.F52
        )
        echo "Starting to read files ..."
        python read_f52.py $ctyfp > c.log

        (
          cd dat
          ../load_csv_pg.sh
          psql census -f ldr.sql >> pg.err
          psql census -f post_process.sql >> pg.err
        )

        echo "done county $ctyfp"
        echo "$ctyfp" >> process.list
      else
#        echo "skipping $ctyfp as it is already loaded"
        skipp=1

      fi

    done # for county ssCCC

    echo "done State $stfp"

    if [ 1 == 1 ]; then
    # test for bad polygons
      echo "
        CREATE INDEX polypt_${stfp}__geom__ind on t1992.polypt_$stfp using GIST(geom);
        CREATE INDEX poly_${stfp}__geom__ind on t1992.poly_$stfp using GIST(the_geom);
        CREATE INDEX polypt_${stfp}__polyid__ind on t1992.polypt_$stfp (cenid,polyid);
        CREATE INDEX poly_${stfp}__polyid__ind on t1992.poly_$stfp (cenid,polyid);
 
        SELECT g.cenid,g.polyid,count(*) as pts 
          FROM t1992.polypt_$stfp p, t1992.poly_$stfp g
          WHERE p.cenid = g.cenid and p.polyid = g.polyid and
            st_intersects(p.geom,g.the_geom)
          GROUP BY 1,2
          HAVING count(*) > 1; " | psql census -t >> badpoly.rpt
    fi

  fi

done # for each state


