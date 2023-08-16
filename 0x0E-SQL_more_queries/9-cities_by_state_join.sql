-- Use the hbtn_0d_usa database
USE hbtn_0d_usa;

-- List cities with their IDs, names, and corresponding state names
SELECT CONCAT(cities.id, ' - ', cities.name, ' - ', states.name) AS city_info
FROM cities
JOIN states ON cities.state_id = states.id
ORDER BY cities.id ASC;
