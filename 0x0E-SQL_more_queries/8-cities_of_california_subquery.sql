-- Use the hbtn_0d_usa database
USE hbtn_0d_usa;

-- Find the state_id of California from the states table
SET @california_state_id = (SELECT id FROM states WHERE name = 'California');

-- List cities of California sorted by cities.id
SELECT * FROM cities WHERE state_id = @california_state_id ORDER BY id ASC;
