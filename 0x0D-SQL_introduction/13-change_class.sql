-- Script to remove records with score <= 5 from the table second_table

-- Connect to the MySQL server
-- Replace 'username' and 'password' with your actual MySQL credentials
-- Replace 'database_name' with the name of your database
USE hbtn_0c_0;

-- Remove records with score <= 5 from the second_table
DELETE FROM second_table
WHERE score <= 5;
