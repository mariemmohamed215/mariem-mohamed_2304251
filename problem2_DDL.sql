-- ============================================================================
-- Alexandria National University - Faculty of Engineering
-- Introduction to Database Systems (Fall 2026) - Lab 4
-- File: problem2_DDL.sql
-- Students:
--   1. A'laa Sherif Ibrahim (ID: 2304249)
--   2. Mariam Mohamed Ali   (ID: 2304251)
-- ============================================================================

DROP DATABASE IF EXISTS library;
CREATE DATABASE library;
USE library;

CREATE TABLE author (
  author_id  INT PRIMARY KEY AUTO_INCREMENT,
  name       VARCHAR(60) NOT NULL,
  country    VARCHAR(40),
  photo_path VARCHAR(255) DEFAULT NULL
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
  publish_year INT DEFAULT 2020,
  author_id    INT NOT NULL,
  publisher_id INT NOT NULL DEFAULT 1,
  category_id  INT NOT NULL DEFAULT 1,
  cover_path   VARCHAR(255) DEFAULT NULL,
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