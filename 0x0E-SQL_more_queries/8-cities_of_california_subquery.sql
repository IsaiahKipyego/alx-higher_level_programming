-- lists all cities of california  in the database
-- select  California cities
SELECT id, name
FROM cities
WHERE state_id = ( -- get the id of California
      SELECT id
      FROM states
      WHERE name = 'California')
ORDER BY id ASC;
