# To-Do_List
CREATE DATABASE `todolist`;

USE todolist;

CREATE TABLE `task` (
  `id` INT AUTO_INCREMENT PRIMARY KEY,
  `title` VARCHAR(255) NOT NULL,
  `description` VARCHAR(255),
  `is_done` BOOLEAN,
  `created_at` INT NOT NULL,
  `updated_at` INT
);

CREATE USER 'user'@'localhost' IDENTIFIED BY 'password';

GRANT SELECT, INSERT, UPDATE, DELETE ON todolist.* TO 'user'@'localhost';