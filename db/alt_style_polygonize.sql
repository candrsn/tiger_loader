-- Alt style polygonize.sql

-- CREATE SCHEMA tgr_work;
DROP TABLE if exists tgr_work.chain;
DROP TABLE if exists tgr_work.polylink;
DROP TABLE if exists tgr_work.polypt;
DROP TABLE if exists tgr_work.polyattr;

CREATE TABLE tgr_work.polypt as ( select * from t1992.polypt_01);
CREATE TABLE tgr_work.polyattr as ( select * from t1992.polyattr_01);

CREATE TABLE tgr_work.chain as (select * from t1992.chain_01);
CREATE TABLE tgr_work.polylink as (
  SELECT cenidl as cenid, polyidl as polyid, tlid
     FROM t1992.polylink_01 
     WHERE polyidl > '' and cenidl > ''
  UNION ALL
  -- grab right polyid's when they don't match the left polyid's
  --    otherwise the previous select got them
  SELECT cenidr as cenid, polyidr as polyid, tlid
     FROM t1992.polylink_01 
     WHERE polyidr > '' and cenidr > '' and
      not (coalesce(polyidl,'') = polyidr and coalesce(cenidl,'') = cenidr)
);
CREATE INDEX polypt_poly_ind on tgr_work.polypt(cenid,polyid);
CREATE INDEX polyattr_poly_ind on tgr_work.polyattr(cenid,polyid);

CREATE INDEX polylink_poly_ind on tgr_work.polylink(cenid,polyid);
CREATE INDEX polylink_tlid_ind on tgr_work.polylink(tlid);
CREATE INDEX chain_tlid_ind on tgr_work.chain(tlid);

DROP TABLE if exists tgr_work.gchain;
CREATE TABLE tgr_work.gchain as (
  SELECT DISTINCT g.tlid, p.cenid, p.polyid, g.geom, st_astext(g.geom)
    FROM
      tgr_work.chain g LEFT OUTER JOIN
      tgr_work.polylink p on (g.tlid = p.tlid)
);
ALTER TABLE tgr_work.gchain drop st_astext;

DROP TABLE if exists tgr_work.gpoly;
CREATE TABLE tgr_work.gpoly (id serial PRIMARY KEY, geom geometry, cenid text, polyid text);
INSERT INTO tgr_work.gpoly (geom, cenid, polyid)
( SELECT St_Polygonize(geom) AS geom, cenid, polyid
 FROM tgr_work.gchain
 group by cenid, polyid
);
UPDATE tgr_work.gpoly set geom = 
   CASE 
    WHEN st_numgeometries(geom) = 1 THEN st_multi(st_geometryn(geom,1))
    ELSE st_multi(st_buffer(geom,0))
   END;


DROP TABLE if exists poly_tmp;
CREATE TEMP TABLE poly_tmp (id serial PRIMARY KEY, geom geometry, cenid text, polyid text, members integer);
INSERT INTO poly_tmp (cenid, polyid, geom, members)
(SELECT p.cenid, p.polyid, St_Polygonize(c.geom) AS geom, count(*) as members
 FROM tgr_work.chain c,
    tgr_work.polylink p
 WHERE c.tlid = p.tlid
 GROUP BY
   p.cenid, p.polyid
 HAVING count(*) > 0  -- must have at least 2 edges to make a polygon
);

SELECT COUNT(*) from poly_tmp;
SELECT cenid, polyid, members, st_numgeometries(geom) from poly_tmp limit 10;

DROP TABLE if exists poly_err;
CREATE TEMP TABLE poly_err as (
SELECT p.cenid, p.polyid, st_astext(St_Polygonize(c.geom)) AS geom, 'Too Few line segments'::text as reason
 FROM tgr_work.chain c,
    tgr_work.polylink p
 WHERE c.tlid = p.tlid
 GROUP BY
   p.cenid, p.polyid
 HAVING count(*) < 1  -- must have at one edge to make a polygon
);

SELECT COUNT(*) from tgr_work.polypt;
SELECT COUNT(*), st_geometrytype(geom) from poly_tmp group by 2;
SELECT COUNT(*), 
  CASE
    WHEN st_numgeometries(geom) = 0 THEN 0
    WHEN st_numgeometries(geom) = 1 THEN 1
    WHEN st_numgeometries(geom) = 2 THEN 2
    WHEN st_numgeometries(geom) > 2 THEN 10
    ELSE -1
  END
  FROM poly_tmp group by 2;


INSERT INTO poly_err (geom, cenid, polyid, reason)
( SELECT st_astext(geom), cenid, polyid, 'lines did not build'::text 
    FROM
      poly_tmp
    WHERE
      st_numgeometries(geom) = 0
);
DELETE FROM poly_tmp 
  WHERE st_numgeometries(geom) = 0;
UPDATE poly_tmp set geom = 
   CASE 
    WHEN st_numgeometries(geom) = 1 THEN st_multi(st_geometryn(geom,1))
    ELSE st_multi(st_buffer(geom,0))
   END;

SELECT COUNT(*), st_geometrytype(geom) from poly_tmp group by 2;

CREATE index poly_tmp__shp__ind on poly_tmp using GIST(geom);
CREATE index polypt__shp__ind on tgr_work.polypt using GIST(geom);

DROP table if exists tgr_work.poly;
CREATE TABLE tgr_work.poly as (
  SELECT pa.*, g.geom
    FROM
      tgr_work.polyattr pa,
      poly_tmp g
    WHERE
      pa.cenid = g.cenid and pa.polyid = g.polyid
);

  
