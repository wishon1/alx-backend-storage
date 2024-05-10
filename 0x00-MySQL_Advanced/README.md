---

# Project: MySQL Advanced

## Concepts
### Advanced SQL
- **Resources:**
  - [MySQL cheatsheet](https://devhints.io/mysql)
  - [MySQL Performance: How To Leverage MySQL Database Indexing](https://www.liquidweb.com/kb/mysql-optimization-how-to-leverage-mysql-database-indexing/)
  - [Stored Procedure](https://www.w3resource.com/mysql/mysql-procedure.php)
  - [Triggers](https://www.w3resource.com/mysql/mysql-triggers.php)
  - [Views](https://www.w3resource.com/mysql/mysql-views.php)
  - [Functions and Operators](https://dev.mysql.com/doc/refman/5.7/en/functions.html)
  - [Trigger Syntax and Examples](https://dev.mysql.com/doc/refman/5.7/en/trigger-syntax.html)
  - [CREATE TABLE Statement](https://dev.mysql.com/doc/refman/5.7/en/create-table.html)
  - [CREATE PROCEDURE and CREATE FUNCTION Statements](https://dev.mysql.com/doc/refman/5.7/en/create-procedure.html)
  - [CREATE INDEX Statement](https://dev.mysql.com/doc/refman/5.7/en/create-index.html)
  - [CREATE VIEW Statement](https://dev.mysql.com/doc/refman/5.7/en/create-view.html)

### Learning Objectives
By the end of this project, you're expected to:
- Explain the creation of tables with constraints.
- Optimize queries by adding indexes.
- Implement stored procedures and functions in MySQL.
- Implement views in MySQL.
- Implement triggers in MySQL.

## Requirements
- **General:**
  - Files executed on Ubuntu 18.04 LTS using MySQL 5.7 (version 5.7.30).
  - All files should end with a new line.
  - All SQL queries should have a comment just before.
  - All files should start with a comment describing the task.
  - All SQL keywords should be in uppercase.
  - A README.md file at the root of the project folder is mandatory.
  - The length of your files will be tested using wc.

## More Info
- **Comments for your SQL file:**
  ```sql
  $ cat my_script.sql
  -- 3 first students in the Batch ID=3
  -- because Batch 3 is the best!
  SELECT id, name FROM students WHERE batch_id = 3 ORDER BY created_at DESC LIMIT 3;
  $
  ```
- Use "container-on-demand" to run MySQL.
- Ask for container Ubuntu 18.04 - Python 3.7.
- Connect via SSH or via the WebTerminal.
- In the container, start MySQL before playing with it:
  ```bash
  $ service mysql start
   * MySQL Community Server 5.7.30 is started
  $
  ```
- To import a SQL dump:
  ```bash
  $ echo "CREATE DATABASE hbtn_0d_tvshows;" | mysql -uroot -p
  Enter password:
  $ curl "https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql" -s | mysql -uroot -p hbtn_0d_tvshows
  Enter password:
  $ echo "SELECT * FROM tv_genres" | mysql -uroot -p hbtn_0d_tvshows
  Enter password:
  id  name
  1   Drama
  2   Mystery
  3   Adventure
  4   Fantasy
  5   Comedy
  6   Crime
  7   Suspense
  8   Thriller
  $
  ```

## Tasks
### 0. We are all unique! (Mandatory)
- Write a SQL script that creates a table users following specific requirements.

### 1. In and not out (Mandatory)
- Write a SQL script that creates a table users following specific requirements.

### 2. Best band ever! (Mandatory)
- Write a SQL script that ranks country origins of bands, ordered by the number of fans.

### 3. Old school band (Mandatory)
- Write a SQL script that lists all bands with Glam rock as their main style, ranked by their longevity.

### 4. Buy buy buy (Mandatory)
- Write a SQL script that creates a trigger that decreases the quantity of an item after adding a new order.

### 5. Email validation to sent (Mandatory)
- Write a SQL script that creates a trigger that resets the attribute valid_email only when the email has been changed.

### 6. Add bonus (Mandatory)
- Write a SQL script that creates a stored procedure AddBonus that adds a new correction for a student.

### 7. Average score (Mandatory)
- Write a SQL script that creates a stored procedure ComputeAverageScoreForUser that computes and stores the average score for a student.

### 8. Optimize simple search (Mandatory)
- Write a SQL script that creates an index idx_name_first on the table names and the first letter of the name.

### 9. Optimize search and score (Mandatory)
- Write a
