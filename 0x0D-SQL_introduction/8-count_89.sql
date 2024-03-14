-- Script to display the number of records with id = 89 in the table first_table

-- Usage: cat 8-count_89.sql | mysql -hlocalhost -uroot -p hbtn_0c_0 | tail -1

-- MySQL command to count the number of records with id = 89 in first_table
SELECT COUNT(*) FROM first_table WHERE id = 89;
