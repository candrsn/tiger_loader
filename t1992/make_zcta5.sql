-- make_zcta5.sql

DROP TABLE if exists tgr_work.chain;
DROP TABLE if exists tgr_work.polylink;
DROP TABLE if exists tgr_work.zchain;
DROP TABLE if exists tgr_work.zpoly;

CREATE TABLE tgr_work.chain as (select * from t1992.chain_01);
CREATE TABLE tgr_work.polylink as (
  SELECT cenidl as cenid, polyidl as polyid, tlid, 'L' as side
     FROM t1992.polylink_01
     WHERE polyidl > '' and cenidl > ''
  UNION
  -- grab right polyid's when they don't match the left polyid's
  --    otherwise the previous select got them
  SELECT cenidr as cenid, polyidr as polyid, tlid, 'R' as side
     FROM t1992.polylink_01
     WHERE polyidr > '' and cenidr > ''
);  -- limit to unique records, using UNION (no ALL)

CREATE INDEX polylink_poly_ind on tgr_work.polylink(polyid,cenid);
CREATE INDEX polylink_tlid_ind on tgr_work.polylink(tlid);
CREATE INDEX chain_tlid_ind on tgr_work.chain(tlid);


DROP TABLE if exists tgr_work.zchain;
CREATE TABLE tgr_work.zchain as (
  SELECT DISTINCT g.tlid, p.cenid, p.polyid,
    CASE
      WHEN p.side = 'L' THEN zipl
      WHEN p.side = 'R' THEN zipr
      ELSE 'unk' END as zip
    FROM
      tgr_work.chain g LEFT OUTER JOIN
      tgr_work.polylink p on (g.tlid = p.tlid)
);

-- determine the dominant ZIP for each poly


DROP TABLE if exists zctapoly_tmp;
CREATE Temp TABLE zctapoly_tmp as (
  SELECT count(*) as cnt, zip, cenid, polyid
    FROM
      tgr_work.zchain
    WHERE zip > ''
    GROUP BY 2,3,4
);
ALTER TABLE zctapoly_tmp add seq serial;
CREATE INDEX zctapoly_tmp__ind on zctapoly_tmp(polyid,cenid);
-- the dominant ZIP for each poly is the most common ZIP,
--   in the case of a tie pick one
DELETE FROM zctapoly_tmp 
  WHERE EXISTS (SELECT 1 FROM zctapoly_tmp z 
      WHERE z.cenid = zctapoly_tmp.cenid and
        z.polyid = zctapoly_tmp.polyid and 
        (zctapoly_tmp.cnt > z.cnt or 
         (zctapoly_tmp.cnt = z.cnt and zctapoly_tmp.seq > z.seq ))
);
-- SELECT * FROM zctapoly_tmp order by cenid,polyid;

DROP TABLE if exists tgr_work.zpoly;
CREATE TABLE tgr_work.zpoly as (
  SELECT p.geom, z.zip as zcta5, p.state, p.county, p.tract, p.ctbna_basic,
    p.cenid, p.polyid,
    CASE
     WHEN z.zip > '' THEN 't'::char(3)
     ELSE NULL END as zstat
    FROM t1992.poly_01 p LEFT OUTER JOIN
      zctapoly_tmp z on (p.cenid = z.cenid and p.polyid = z.polyid)
);

-- ***************************************************************
-- handle Counties with a single ZIP code
DROP TABLE if exists county_zip;
CREATE TEMP TABLE County_zip as (
  SELECT c.county, z.zcta5
  FROM
  (SELECT count(*) as cnt, county
    FROM 
      (SELECT county, zcta5,  count(*) as polys
         FROM tgr_work.zpoly
         WHERE zcta5 > ''
         GROUP BY 1,2
      ) as d
    GROUP BY 2
    HAVING count(*) = 1 ) as c,
    (SELECT county, zcta5, count(*) 
       FROM tgr_work.zpoly
       WHERE zcta5 > ''  
       GROUP BY 1,2
     ) as z
    WHERE z.county = c.county
 );
UPDATE tgr_work.zpoly set
    zcta5 = (select zcta5 from county_zip c where c.county = zpoly.county),
    zstat = 'ci'
    WHERE
      county in (select county from county_zip) and
      zcta5 is null and
      zstat is null;

-- handle Tracts with a single ZIP code
DROP TABLE if exists tract_zip;
CREATE TEMP TABLE tract_zip as (
  SELECT c.county, c.tract, z.zcta5
  FROM
  (SELECT count(*) as cnt, county, tract
    FROM 
      (SELECT county, tract, zcta5,  count(*) as polys
         FROM tgr_work.zpoly
         WHERE zcta5 > ''
         GROUP BY 1,2,3
      ) as d
    GROUP BY 2,3
    HAVING count(*) = 1 ) as c,
    (SELECT county, tract, zcta5, count(*) 
       FROM tgr_work.zpoly
       WHERE zcta5 > ''  
       GROUP BY 1,2,3
     ) as z
    WHERE z.county = c.county and z.tract = c.tract
 );
UPDATE tgr_work.zpoly set
    zcta5 = (select zcta5 from tract_zip c where c.county = zpoly.county and
          c.tract = zpoly.tract),
    zstat = 'ti'
    WHERE
      (county,tract) in (select county,tract from tract_zip) and
      zcta5 is null and
      zstat is null;

-- handle BlockGroups with a single ZIP code
DROP TABLE if exists bg_zip;
CREATE TEMP TABLE bg_zip as (
  SELECT c.county, c.tract, c.bg, z.zcta5
  FROM
  (SELECT count(*) as cnt, county, tract, bg
    FROM 
      (SELECT county, tract, substr(ctbna_basic,1,1) as bg, zcta5,  count(*) as polys
         FROM tgr_work.zpoly
         WHERE zcta5 > ''
         GROUP BY 1,2,3,4
      ) as d
    GROUP BY 2,3,4
    HAVING count(*) = 1 ) as c,
    (SELECT county, tract, substr(ctbna_basic,1,1) as bg, zcta5, count(*) 
       FROM tgr_work.zpoly
       WHERE zcta5 > ''  
       GROUP BY 1,2,3,4
     ) as z
    WHERE z.county = c.county and z.tract = c.tract and z.bg = c.bg
 );
UPDATE tgr_work.zpoly set
    zcta5 = (select zcta5 from bg_zip c where c.county = zpoly.county and
          c.tract = zpoly.tract and c.bg = substr(zpoly.ctbna_basic,1,1)),
    zstat = 'bgi'
    WHERE
      (county,tract,substr(ctbna_basic,1,1)) in (select county,tract,bg from bg_zip) and
      zcta5 is null and
      zstat is null;

-- handle Block with a single ZIP code
DROP TABLE if exists block_zip;
CREATE TEMP TABLE block_zip as (
  SELECT c.county, c.tract, c.ctbna_basic, z.zcta5
  FROM
  (SELECT count(*) as cnt, county, tract, ctbna_basic
    FROM 
      (SELECT county, tract, ctbna_basic, zcta5,  count(*) as polys
         FROM tgr_work.zpoly
         WHERE zcta5 > ''
         GROUP BY 1,2,3,4
      ) as d
    GROUP BY 2,3,4
    HAVING count(*) = 1 ) as c,
    (SELECT county, tract, ctbna_basic, zcta5, count(*) 
       FROM tgr_work.zpoly
       WHERE zcta5 > ''  
       GROUP BY 1,2,3,4
     ) as z
    WHERE z.county = c.county and z.tract = c.tract and z.ctbna_basic = c.ctbna_basic
 );
UPDATE tgr_work.zpoly set
    zcta5 = (select zcta5 from block_zip c where c.county = zpoly.county and
          c.tract = zpoly.tract and c.ctbna_basic = zpoly.ctbna_basic),
    zstat = 'bi'
    WHERE
      (county,tract,ctbna_basic) in (select county,tract,ctbna_basic from block_zip) and
      zcta5 is null and
      zstat is null;






-- Grow ZIPcodes within a block
CREATE INDEX zpoly__geom__ind on tgr_work.zpoly USING GIST(geom);
DROP TABLE if exists block_neighbors;
CREATE TEMP TABLE block_neighbors as (
  SELECT p.cenid, p.polyid, z.zcta5, 
     CASE
       WHEN p.county = z.county and p.tract = z.tract and z.ctbna_basic = p.ctbna_basic THEN 'same block'::char(15)
       WHEN p.county = z.county and p.tract = z.tract and substr(z.ctbna_basic,1,1) = substr(p.ctbna_basic,1,1) THEN 'same BG'::char(15)
       WHEN p.county = z.county and p.tract = z.tract THEN 'same tract'::char(15)
       WHEN p.county = z.county THEN 'same county'::char(15)
       ELSE 'different' END as rel,
     st_length(st_boundary(p.geom)) as len,
     sum(st_length(st_intersection(p.geom, z.geom))) as ilen,
     count(*) as members
    FROM
      tgr_work.zpoly p,  -- empty zcta
      tgr_work.zpoly z   -- populated zcta
    WHERE
      z.zcta5 > '' and
      p.zcta5 is NULL and
      st_intersects(p.geom, z.geom)
    GROUP BY 1,2,3,4,5
);
ALTER TABLE block_neighbors add seq serial;
ALTER TABLE block_neighbors add best_choice integer;

-- find the longest ilen in the same ZIP Code
DROP TABLE long_block;
CREATE TEMP TABLE long_block as (
  SELECT cenid, polyid, zcta5, max(ilen/len) as plen, max(seq) as seq
    FROM block_neighbors
    GROUP BY 1,2,3
);
CREATE INDEX long_block__poly__ind on long_block(polyid,cenid);

DROP TABLE long_block_uniq;
CREATE TEMP TABLE long_block_uniq as (
  SELECT cenid, polyid, count(*)
    FROM
      long_block
    GROUP BY 1,2
    HAVING COUNT(*) = 1
);
UPDATE tgr_work.zpoly set
    zcta5 = n.zcta5,
    zstat = 'zu'
   FROM
    long_block n
   WHERE
     zpoly.zcta5 is NULL and
     zpoly.cenid = n.cenid and
     zpoly.polyid = n.polyid and
     (n.cenid,n.polyid) in (SELECT cenid,polyid FROM long_block_uniq)
;


SELECT * from long_block order by cenid, polyid limit 5;

SELECT cenid, polyid, rel
SELECT * from block_neighbors order by cenid,polyid limit 3;



UPDATE tgr_work.zpoly set
   zcta5 = i.zcta5,
   zstat = 'gb'
   FROM
    block_neighbors i
   WHERE
    i.cenid = zpoly.cenid and i.polyid = zpoly.polyid and
    i.best_choice = 1
;

-- *************************************************8
UPDATE tgr_work.zpoly set geom = 
   CASE 
    WHEN st_numpoints(geom) = 0 THEN NULL
    WHEN st_numgeometries(geom) = 1 THEN st_multi(st_geometryn(geom,1))
    ELSE st_multi(st_buffer(geom,0))
   END
  WHERE st_geometrytype(geom) <> 'ST_MultiPolygon';

DROP TABLE if exists t1992.zcta_01;
CREATE TABLE t1992.zcta_01 as (
  SELECT * FROM tgr_work.zpoly
 );


