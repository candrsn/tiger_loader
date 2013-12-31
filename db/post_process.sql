-- post_process.sql

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
  SELECT pa.*, g.the_geom
    FROM
      work.polyattr pa,
      work.polypt p,
      poly_tmp g
    WHERE
      st_intersects(p.geom, g.the_geom) and
      pa.cenid = p.cenid and pa.polyid = p.polyid
);

  

-- CREATE SCHMES t1992;
CREATE TABLE if not exists t1992.Addr ( like work.Addr );
CREATE TABLE if not exists t1992.Addr_02 () inherits (t1992.Addr );
INSERT INTO t1992.Addr_02 ( SELECT * from work.Addr );
DROP TABLE work.Addr;


-- CREATE SCHMES t1992;
CREATE TABLE if not exists t1992.chain ( like work.chain );
CREATE TABLE if not exists t1992.chain_02 () inherits (t1992.chain );
INSERT INTO t1992.chain_02 ( SELECT * from work.chain );
DROP TABLE work.chain;


-- CREATE SCHMES t1992;
CREATE TABLE if not exists t1992.Featname ( like work.Featname );
CREATE TABLE if not exists t1992.Featname_02 () inherits (t1992.Featname );
INSERT INTO t1992.Featname_02 ( SELECT * from work.Featname );
DROP TABLE work.Featname;


-- CREATE SCHMES t1992;
CREATE TABLE if not exists t1992.FeatnameLink ( like work.FeatnameLink );
CREATE TABLE if not exists t1992.FeatnameLink_02 () inherits (t1992.FeatnameLink );
INSERT INTO t1992.FeatnameLink_02 ( SELECT * from work.FeatnameLink );
DROP TABLE work.FeatnameLink;


-- CREATE SCHMES t1992;
CREATE TABLE if not exists t1992.PolyAttr ( like work.PolyAttr );
CREATE TABLE if not exists t1992.PolyAttr_02 () inherits (t1992.PolyAttr );
INSERT INTO t1992.PolyAttr_02 ( SELECT * from work.PolyAttr );
DROP TABLE work.PolyAttr;


-- CREATE SCHMES t1992;
CREATE TABLE if not exists t1992.polyLink ( like work.polyLink );
CREATE TABLE if not exists t1992.polyLink_02 () inherits (t1992.polyLink );
INSERT INTO t1992.polyLink_02 ( SELECT * from work.polyLink );
DROP TABLE work.polyLink;


-- CREATE SCHMES t1992;
CREATE TABLE if not exists t1992.PolyPt ( like work.PolyPt );
CREATE TABLE if not exists t1992.PolyPt_02 () inherits (t1992.PolyPt );
INSERT INTO t1992.PolyPt_02 ( SELECT * from work.PolyPt );
DROP TABLE work.PolyPt;


-- CREATE SCHMES t1992;
CREATE TABLE if not exists t1992.poly ( like work.poly );
CREATE TABLE if not exists t1992.poly_02 () inherits (t1992.poly );
INSERT INTO t1992.poly_02 ( SELECT * from work.poly );
DROP TABLE work.poly;

