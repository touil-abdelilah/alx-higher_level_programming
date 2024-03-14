# What is Database & SQL?

## Introduction
In the world of software development and data management, understanding databases and SQL (Structured Query Language) is crucial. Databases serve as organized collections of data, while SQL provides a standardized language for interacting with and managing that data. This README provides an overview of databases, SQL, and their key concepts.

## What's a Database?
A database is a structured collection of data that is organized and stored electronically. It is designed to efficiently manage, retrieve, and manipulate data based on various criteria. Databases are widely used in applications ranging from simple websites to large-scale enterprise systems.

## What's a Relational Database?
A relational database is a type of database that stores and organizes data in tables consisting of rows and columns. It uses a relational model to establish relationships between different sets of data. The most common relational database management system (RDBMS) is MySQL, though there are others like PostgreSQL, Oracle, SQL Server, etc.

## What Does SQL Stand For?
SQL stands for Structured Query Language. It is a domain-specific language used for managing and manipulating relational databases. SQL provides a set of commands for querying, updating, and managing data within a database.

## What's MySQL?
MySQL is an open-source relational database management system (RDBMS) that uses SQL. It is widely used in web development and other applications due to its reliability, performance, and ease of use. MySQL supports various operating systems and programming languages.

## How to Create a Database in MySQL
In MySQL, you can create a new database using the `CREATE DATABASE` statement followed by the database name. For example:
```sql
CREATE DATABASE mydatabase;
```

## What Does DDL and DML Stand For?
- DDL: Data Definition Language. It includes SQL commands used to define, modify, and delete database objects like tables, indexes, and views.
- DML: Data Manipulation Language. It includes SQL commands used to manipulate data within tables, such as inserting, updating, deleting, and querying records.

## How to CREATE or ALTER a Table
To create a new table in MySQL, you use the `CREATE TABLE` statement followed by the table name and its columns. For example:
```sql
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50),
    email VARCHAR(100)
);
```
To alter an existing table, you use the `ALTER TABLE` statement followed by the modifications you want to make.

## How to SELECT Data from a Table
To retrieve data from a table, you use the `SELECT` statement followed by the columns you want to retrieve and the table name. For example:
```sql
SELECT * FROM users;
```

## How to INSERT, UPDATE, or DELETE Data
- `INSERT`: Adds new records to a table.
- `UPDATE`: Modifies existing records in a table.
- `DELETE`: Removes records from a table.
```sql
INSERT INTO users (username, email) VALUES ('john_doe', 'john@example.com');
UPDATE users SET email = 'new_email@example.com' WHERE id = 1;
DELETE FROM users WHERE id = 1;
```

## What Are Subqueries?
Subqueries (also known as nested queries) are SQL queries nested within another query. They allow you to retrieve data based on the result of another query. Subqueries are often used in `SELECT`, `INSERT`, `UPDATE`, and `DELETE` statements.

## How to Use MySQL Functions
MySQL provides a variety of built-in functions for performing operations on data. These functions include mathematical functions, string functions, date functions, and more. For example:
```sql
SELECT SUM(sales) FROM transactions;
SELECT UPPER(name) FROM products;
SELECT YEAR(date_column) FROM orders;
```

