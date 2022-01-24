CREATE DATABASE vaxer;
USE vaxer;
# for patient to login into the interface
CREATE TABLE login (email VARCHAR(50) PRIMARY KEY, password VARCHAR(25));
# for patient to register for the vaccination
CREATE TABLE registration(uidai BIGINT PRIMARY KEY, first_name VARCHAR(25), last_name VARCHAR(25), age INT, gender ENUM('M','F'), type INT, centre INT, slot INT, email VARCHAR(50));
# a list of vaccine options with availability
CREATE TABLE vaccines(vacc_id INT PRIMARY KEY, name VARCHAR(25), status CHAR(1));
# a list of vaccination centres
CREATE TABLE centres(center_id INT PRIMARY KEY, name VARCHAR(50), address VARCHAR(1000), district VARCHAR(50), state VARCHAR(20), pincode INT);
