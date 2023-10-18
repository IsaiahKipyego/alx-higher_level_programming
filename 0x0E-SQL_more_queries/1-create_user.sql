-- creates a user and assign password
-- create user
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost'
IDENTIFIED BY 'user_0d_1_pwd';
-- give permission
GRANT ALL PRIVILEGES ON *.*
TO 'user_0d_1'@'localhost';
