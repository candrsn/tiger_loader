-- bad_poly.sh

 CREATE TEMP TABLE poly as (
  SELECT st_astext(st_box2d(the_geom))||st_astext(st_startpoint(st_exteriorring(the_geom))) as id, cenid, polyid, the_geom
    FROM t1992.poly_01
 );

 CREATE TEMP TABLE dups as (
  SELECT p.id, p.cenid, p.polyid, i.cnt as id_cnt, c.cnt as poly_cnt
    FROM
      poly p,
      ( SELECT cenid, polyid, count(*) as cnt 
         FROM poly
         GROUP by 1,2 ) as c,
      ( SELECT id, count(*) as cnt 
         FROM poly
         GROUP by 1 ) as i
   WHERE
     p.id = i.id and
     p.cenid = c.cenid and 
     p.polyid = c.polyid
 );
 CREATE INDEX dupsid_ind on dups(id);
 CREATE INDEX dupspoly_ind on dups(cenid,polyid);

-- a table of all repeating IDs
DROP TABLE if exists work.cull;
 CREATE TABLE work.cull as (
   SELECT id, cenid, polyid, the_geom
     FROM
       poly p
     WHERE exists (SELECT 1 from dups d 
        WHERE 
          d.id = p.id and d.id_cnt > 1)
  );

-- remove from list those whose cenid,polyid matches a different (id) that is not repreating
 DELETE FROM work.cull 
   WHERE 1 = (SELECT 1 from dups d where id_cnt = 1 and 
     d.cenid = cull.cenid and
     d.polyid = cull.polyid and
     d.id = cull.id);

 CREATE INDEX cull__ind on work.cull(cenid,polyid);
 DELETE from poly 
   WHERE (cenid,polyid,st_makeline(st_startpoint(st_boundary(the_geom)),st_line_interpolate_point(st_exteriorring(the_geom),0.5))) in
   (SELECT cenid, polyid, id from work.cull);


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

