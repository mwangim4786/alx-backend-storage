-- script that creates a table with unique users 
-- script can be executed on any database, use ENUM
CREATE TABLE IF NOT EXISTS `users` (
    `id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `email` VARCHAR(255) NOT NULL UNIQUE,
    `name` VARCHAR(255),
    `country` ENUM('US', 'CO', 'TN') NOT NULL
);
