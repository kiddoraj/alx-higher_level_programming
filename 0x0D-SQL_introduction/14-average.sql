-- Script to compute the average score of all records in the table second_table

-- Connect to the MySQL server
-- Replace 'username' and 'password' with your actual MySQL credentials
-- Replace 'database_name' with the name of your database
USE hbtn_0c_0;

-- Compute the average score of all records
SELECT AVG(score) AS average
FROM second_table;
