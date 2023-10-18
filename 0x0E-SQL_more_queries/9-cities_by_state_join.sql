-- lists all cities in the database
-- list cities
SELECT cities.id, cities.name, states.name
FROM cities
JOIN states -- join the two tables
ON cities.state_id = states.id
ORDER BY cities.id ASC;
