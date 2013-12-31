-- zcta5_expansion rules.sql

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

-- find the longest ilen in the same relationship
DROP TABLE long_block;
CREATE TEMP TABLE long_block as (
  SELECT cenid, polyid, rel, zcta5, max(ilen/len) as plen, max(seq) as seq
    FROM block_neighbors
    GROUP BY 1,2,3,4
);
CREATE INDEX long_block__poly__ind on long_block(polyid,cenid);

DROP TABLE long_block_uniq;
CREATE TEMP TABLE long_block_uniq as (
  SELECT cenid, polyid, rel, count(*), max(plen) as plen
    FROM
      long_block
    GROUP BY 1,2,3
);
UPDATE tgr_work.zpoly set
    zcta5 = n.zcta5,
    zstat = 'gbu2'
   FROM
    long_block n
   WHERE
     zpoly.zcta5 is NULL and
     zpoly.cenid = n.cenid and
     zpoly.polyid = n.polyid and
     n.rel = 'same tract' and
     (n.cenid,n.polyid) in (SELECT cenid,polyid FROM long_block_uniq where count = 1)
;
UPDATE tgr_work.zpoly set
    zcta5 = n.zcta5,
    zstat = 'gb2'
   FROM
    long_block n
   WHERE
     zpoly.zcta5 is NULL and
     zpoly.cenid = n.cenid and
     zpoly.polyid = n.polyid and
     n.rel = 'same tract' and
     (n.cenid,n.polyid,plen) in (SELECT cenid,polyid,plen FROM long_block_uniq where count > 1)
;






-- Repeat Growth by Block - until clear



UPDATE tgr_work.zpoly set
   zcta5 = i.zcta5,
   zstat = 'gb'
   FROM
    block_neighbors i
   WHERE
    i.cenid = zpoly.cenid and i.polyid = zpoly.polyid and
    i.best_choice = 1
;

-- cd wtmp
-- pgsql2shp census tgr_work.zpoly
-- qgis ../zpoly.qgs
