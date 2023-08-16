-- Create database hbtn_0d_2 if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- Create or update MySQL user user_0d_2
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- Grant SELECT privilege to user_0d_2 only on hbtn_0d_2 database
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';

-- Refresh privileges to apply changes
FLUSH PRIVILEGES;
