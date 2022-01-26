# create database
CREATE DATABASE IF NOT EXISTS vaxer;
# open the database
USE vaxer;
# for patient to login
CREATE TABLE IF NOT EXISTS login (email VARCHAR(50) PRIMARY KEY, pass VARCHAR(25) NOT NULL);
# a list of vaccine options
CREATE TABLE IF NOT EXISTS vaccines (vacc_id INT PRIMARY KEY, name VARCHAR(25) UNIQUE NOT NULL, status ENUM('Y', 'N'));
# a list of vaccination centers
CREATE TABLE IF NOT EXISTS centers (center_id INT PRIMARY KEY, name VARCHAR(50) NOT NULL, address VARCHAR(500) NOT NULL, district VARCHAR(50) NOT NULL, state VARCHAR(20) NOT NULL, pincode INT NOT NULL, UNIQUE(address, district, state));
# for patient to register for the vaccination
CREATE TABLE IF NOT EXISTS registration (uidai BIGINT PRIMARY KEY, first_name VARCHAR(25) NOT NULL, last_name VARCHAR(25) NOT NULL, age INT NOT NULL, gender ENUM('M','F'), vaccine INT REFERENCES vaccines ON DELETE RESTRICT ON UPDATE CASCADE, center INT REFERENCES centers ON DELETE RESTRICT ON UPDATE CASCADE, slot ENUM('1', '2', '3', '4'), email VARCHAR(50) UNIQUE REFERENCES login ON DELETE CASCADE ON UPDATE CASCADE);
