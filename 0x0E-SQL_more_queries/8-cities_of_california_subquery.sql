-- Select all cities of California using a subquery to find the state_id for California
SELECT * 
FROM cities
WHERE state_id = (SELECT id FROM states WHERE name = 'California')
ORDER BY id ASC;
