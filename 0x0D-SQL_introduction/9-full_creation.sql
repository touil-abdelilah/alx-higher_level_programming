-- Script to create a table second_table in the database hbtn_0c_0 and add multiple rows

-- Usage: cat 9-full_creation.sql | mysql -hlocalhost -uroot -p hbtn_0c_0

-- MySQL command to create the table if not exists
CREATE TABLE IF NOT EXISTS second_table (
    id INT,
    name VARCHAR(256),
    score INT
);

-- MySQL command to insert rows into the table
INSERT INTO second_table (id, name, score) VALUES
    (1, 'John', 10),
    (2, 'Alex', 3),
    (3, 'Bob', 14),
    (4, 'George', 8);

