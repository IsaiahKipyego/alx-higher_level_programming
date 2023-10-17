-- show top 3 cities temperature during month of July and August
-- ordered by temp
SELECT city, AVG(value) as avg_temp
FROM temperatures
WHERE month = 7 OR month = 8
GROUP BY city
ORDER BY avg_temp
DESC LIMIT 3;
