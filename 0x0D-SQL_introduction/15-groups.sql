-- Script to list the number of records with the same score in the table second_table

-- Connect to the MySQL server
-- Replace 'username' and 'password' with your actual MySQL credentials
-- Replace 'database_name' with the name of your database
USE hbtn_0c_0;

-- List the number of records with the same score and sort by the number of records (descending)
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;
