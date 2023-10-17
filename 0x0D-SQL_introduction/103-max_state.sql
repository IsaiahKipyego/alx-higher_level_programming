-- show maximum temperature of each state
-- list max temperatures
SELECT state, MAX(value) as max_temp
FROM temperatures
GROUP BY state
ORDER BY state ASC;
