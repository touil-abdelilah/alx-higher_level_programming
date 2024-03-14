-- Script to list all records of the table second_table without rows without a name value

-- MySQL command to select records with a name value and order by descending score
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
