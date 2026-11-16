-- LAB 3 - Problem 2: Library with Authors and Books only
DROP DATABASE IF EXISTS library_lab3;
CREATE DATABASE library_lab3;
USE library_lab3;

CREATE TABLE author (
    author_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(60) NOT NULL,
    country VARCHAR(40)
);

CREATE TABLE book (
    book_id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(100) NOT NULL,
    price DECIMAL(8,2) NOT NULL,
    author_id INT NOT NULL,
    CONSTRAINT fk_book_author
        FOREIGN KEY (author_id) REFERENCES author(author_id)
        ON DELETE CASCADE
);
