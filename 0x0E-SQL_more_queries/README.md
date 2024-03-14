# SQL - More queries

An overview of MySQL basics, covering essential topics such as creating users, granting permissions, working with constraints, using subqueries, performing join operations, and understanding SQL techniques. It also includes references to MySQL cheat sheets, tutorials, and style guides for further learning.

## How To Create a New User and Grant Permissions in MySQL

To create a new user and grant permissions in MySQL, follow these steps:

1. **Log in to MySQL**: Use the MySQL client or command-line interface to log in as a user with sufficient privileges, typically the root user.
   ```bash
   mysql -u root -p
   ```

2. **Create a New User**: Use the `CREATE USER` command to create a new MySQL user account.
   ```sql
   CREATE USER 'username'@'localhost' IDENTIFIED BY 'password';
   ```

3. **Grant Privileges**: Grant necessary privileges to the user for specific databases or tables.
   ```sql
   GRANT SELECT, INSERT, UPDATE ON database_name.* TO 'username'@'localhost';
   ```

4. **Flush Privileges**: After granting privileges, flush the privileges to ensure changes take effect immediately.
   ```sql
   FLUSH PRIVILEGES;
   ```

## How To Use MySQL GRANT Statement To Grant Privileges To a User

The `GRANT` statement is used to grant specific privileges to a user in MySQL. For example:
```sql
GRANT SELECT, INSERT, UPDATE ON database_name.* TO 'username'@'localhost';
```

## MySQL Constraints

MySQL constraints are rules that enforce data integrity and define limitations on the values that can be inserted into columns. Common constraints include `NOT NULL`, `UNIQUE`, `PRIMARY KEY`, `FOREIGN KEY`, and `CHECK`.

## SQL Technique: Subqueries

Subqueries, also known as nested queries, are SQL queries nested within another query. They can be used to retrieve data based on conditions or perform operations on the result set of the outer query.

## Basic Query Operation: The Join

Joins are SQL operations used to combine rows from two or more tables based on a related column between them. Common join types include `INNER JOIN`, `LEFT JOIN`, `RIGHT JOIN`, and `FULL JOIN`.

## SQL Technique: Multiple Joins and the DISTINCT Keyword

Multiple joins allow you to join more than two tables in a single query, while the `DISTINCT` keyword removes duplicate rows from the result set of a query.

## SQL Technique: Join Types

Join types determine how records from two or more tables are combined. They include `INNER JOIN`, `LEFT JOIN`, `RIGHT JOIN`, and `FULL JOIN`, each with its own behavior and use cases.

## SQL Technique: UNION and MINUS

`UNION` combines the result sets of two or more `SELECT` statements into a single result set, while `MINUS` returns the difference between two result sets.

## MySQL Cheat Sheet

A MySQL cheat sheet provides quick reference to commonly used MySQL commands, syntax, and functions, making it useful for both beginners and experienced users.

## The Seven Types of SQL Joins

The seven types of SQL joins include `INNER JOIN`, `LEFT JOIN`, `RIGHT JOIN`, `FULL JOIN`, `CROSS JOIN`, `SELF JOIN`, and `NATURAL JOIN`, each serving different purposes and producing different results.

## MySQL Tutorial

A MySQL tutorial provides step-by-step guidance on various MySQL concepts, operations, and best practices, making it ideal for beginners to learn MySQL from scratch.

## SQL Style Guide

An SQL style guide outlines recommended conventions and best practices for writing SQL queries, ensuring consistency, readability, and maintainability across database projects.

## MySQL 8.0 SQL Statement Syntax

MySQL 8.0 SQL statement syntax defines the grammar and rules for writing valid MySQL queries and commands, covering various aspects such as data manipulation, data definition, and data control.

