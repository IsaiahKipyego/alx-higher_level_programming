-- display mean temperatures ordered by temp
-- diplay mean
SELECT city, AVG(value) as avg_temp
FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;
