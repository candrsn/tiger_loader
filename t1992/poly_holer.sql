-- poly_holer.sql - rewritten for state %01%

-- When only a outer ring exists for a polygon find the conflicting other portion
--   and compute the difference

DROP TABLE if exists tgr_work.ppoly;
CREATE TABLE tgr_work.ppoly as (
  SELECT * from t1992.poly_%01%);
CREATE INDEX ppoly__geom__ind on tgr_work.ppoly using GIST(geom);

UPDATE tgr_work.ppoly set geom = 
   CASE 
    WHEN st_numpoints(geom) = 0 THEN NULL
    WHEN st_numgeometries(geom) = 1 THEN st_multi(st_geometryn(geom,1))
    ELSE st_multi(st_buffer(geom,0))
   END
  WHERE st_geometrytype(geom) <> 'ST_MultiPolygon';

CREATE TEMP table olap as ( select c.cenid, c.polyid, c.geom,
   p.cenid as parent_cenid, p.polyid as parent_polyid
   from tgr_work.ppoly c, tgr_work.ppoly p
   where
    st_intersects(c.geom, p.geom) and
    st_contains(p.geom, c.geom) and
    c.polyid <> p.polyid
);

DROP TABLE if exists parent_olap;
CREATE TEMP TABLE parent_olap as (
  SELECT parent_cenid, parent_polyid, st_union(geom) as geom
    FROM olap
    GROUP BY 1,2
);
CREATE INDEX parent_olap__ind on parent_olap(parent_cenid, parent_polyid);

update t1992.poly_%01% set
    geom = st_difference(poly_%01%.geom, p.geom)
  FROM
    parent_olap p
  WHERE
    p.parent_cenid = poly_%01%.cenid and
    p.parent_polyid = poly_%01%.polyid
;


