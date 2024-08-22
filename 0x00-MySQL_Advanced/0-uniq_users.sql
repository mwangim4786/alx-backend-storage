--- script that creates a table with unique users 
DROP TABLE IF EXISTS users;
CREATE TABLE users (
	id INT NOT NULL AUTO_INCREAMENT PRIMARY KEY,
	email VARCHAR(255) NOT NULL INIQUE,
	name VARCHAR(255)
);
