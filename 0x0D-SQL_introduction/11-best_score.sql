-- Script to list records with score >= 10 from the table second_table

-- List records with score >= 10 from the second_table
SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;
