-- Lists all records except rows without name value of the table second_table
-- display score and name in descending score
SELECT score, name FROM second_table WHERE name != "NULL" ORDER BY score DESC;
