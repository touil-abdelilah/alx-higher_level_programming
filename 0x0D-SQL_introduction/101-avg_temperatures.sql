-- Import the provided table dump into the hbtn_0c_0 database
-- (Assuming the file name is "table_dump.sql")
-- mysql -hlocalhost -uroot -p hbtn_0c_0 < table_dump.sql

-- Script to calculate the average temperature (Fahrenheit) by city ordered by temperature (descending)
SELECT city, AVG(temperature) AS avg_temp
FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;
