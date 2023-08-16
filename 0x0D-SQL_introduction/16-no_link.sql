-- Script to list records of the table second_table with non-empty names

-- Connect to the MySQL server
-- Replace 'username' and 'password' with your actual MySQL credentials
-- Replace 'database_name' with the name of your database
USE hbtn_0c_0;

-- List records of the second_table with non-empty names, ordered by descending score
SELECT score, name
FROM second_table
WHERE name IS NOT NULL AND name <> ''
ORDER BY score DESC;
