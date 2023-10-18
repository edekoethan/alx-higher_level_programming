Database Management Scripts Readme
This repository contains a set of scripts designed to manage and interact with a MySQL database. These scripts perform various tasks, such as listing databases, creating and deleting databases, creating and querying tables, and inserting and retrieving data. Each script is documented briefly below.

Task 0: List Databases
Script: 0-list_databases.sql
Description: This script lists all databases on your MySQL server using the SHOW DATABASES statement.
Task 1: Create a Database
Script: 1-create_database_if_not_exists.sql
Description: This script creates the database named hbtn_0c_0 on your MySQL server if it does not already exist. It does not use the SELECT or SHOW statements.
Task 2: Delete a Database
Script: 2-delete_database_if_exists.sql
Description: This script deletes the database named hbtn_0c_0 from your MySQL server if it exists. It does not use the SELECT or SHOW statements.
Task 3: List Tables
Script: 3-list_tables.sql
Description: This script lists all the tables in a specified database (given as an argument to the mysql command).
Task 4: First Table
Script: 4-first_table.sql
Description: This script creates a table named first_table with columns id (INT) and name (VARCHAR(256)) in the current database. If the table already exists, it will not fail. It does not use the SELECT or SHOW statements.
Task 5: Full Description
Script: 5-full_description.sql
Description: This script prints the full description of the first_table from the specified database. It does not use the DESCRIBE or EXPLAIN statements.
Task 6: List All in Table
Script: 6-list_all_in_table.sql
Description: This script lists all rows of the first_table in the specified database. It retrieves all fields in each row.
Task 7: First Add
Script: 7-first_add.sql
Description: This script inserts a new row into the first_table in the specified database. The new row has id = 89 and name = Best School.
Task 8: Count 89
Script: 8-count_89.sql
Description: This script displays the number of records in the first_table with id = 89 in the specified database.
Task 9: Full Creation
Script: 9-full_creation.sql
Description: This script creates a table named second_table with columns id (INT), name (VARCHAR(256)), and score (INT) in the specified database. If the table already exists, it will not fail. It inserts multiple records into the second_table.
For each task, follow the provided script's instructions and use the specified arguments to interact with your MySQL server. These scripts are intended to help you manage your MySQL database efficiently.
