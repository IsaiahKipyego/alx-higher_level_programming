-- creates a db hbtn_0d_usa with table states
-- create database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa; -- Switch to database
CREATE TABLE IF NOT EXISTS states
(id INT PRIMARY KEY AUTO_INCREMENT,
name VARCHAR(256) NOT NULL);
