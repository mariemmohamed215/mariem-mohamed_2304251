DROP DATABASE IF EXISTS library;
CREATE DATABASE library;
USE library;

CREATE TABLE author (
  author_id INT PRIMARY KEY AUTO_INCREMENT,
  name      VARCHAR(60) NOT NULL,
  country   VARCHAR(40)
);
CREATE TABLE publisher (
  publisher_id INT PRIMARY KEY AUTO_INCREMENT,
  name         VARCHAR(60) NOT NULL,
  country      VARCHAR(40)
);
CREATE TABLE category (
  category_id INT PRIMARY KEY AUTO_INCREMENT,
  name        VARCHAR(40) NOT NULL
);
CREATE TABLE book (
  book_id      INT PRIMARY KEY AUTO_INCREMENT,
  title        VARCHAR(100) NOT NULL,
  price        DECIMAL(8,2),
  publish_year INT,
  author_id    INT NOT NULL,
  publisher_id INT NOT NULL,
  category_id  INT NOT NULL,
  FOREIGN KEY (author_id)    REFERENCES author(author_id)       ON DELETE CASCADE,
  FOREIGN KEY (publisher_id) REFERENCES publisher(publisher_id),
  FOREIGN KEY (category_id)  REFERENCES category(category_id)
);
CREATE TABLE member (
  member_id INT PRIMARY KEY AUTO_INCREMENT,
  name      VARCHAR(60) NOT NULL,
  email     VARCHAR(80),
  join_date DATE
);
CREATE TABLE loan (
  loan_id     INT PRIMARY KEY AUTO_INCREMENT,
  book_id     INT NOT NULL,
  member_id   INT NOT NULL,
  loan_date   DATE NOT NULL,
  return_date DATE NULL,
  FOREIGN KEY (book_id)   REFERENCES book(book_id)     ON DELETE CASCADE,
  FOREIGN KEY (member_id) REFERENCES member(member_id)
);
