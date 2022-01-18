CREATE DATABASE vaxer;
USE vaxer;
CREATE TABLE login (email VARCHAR(50) PRIMARY KEY, password VARCHAR(25));
CREATE TABLE registration(uidai BIGINT PRIMARY KEY, centre INT, slot INT);
CREATE TABLE vaccines(vacc_id INT PRIMARY KEY, name VARCHAR(25), status CHAR(1));
CREATE TABLE centres(center_id INT PRIMARY KEY, name VARCHAR(50), address VARCHAR(1000), district VARCHAR(50), state VARCHAR(20), pincode INT);
CREATE TABLE uidai(uidai BIGINT PRIMARY KEY, first_name VARCHAR(25), last_name VARCHAR(25), age INT, gender CHAR(1));
CREATE TABLE records(uidai BIGINT PRIMARY KEY, dose INT);
