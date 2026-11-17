-- ============================================================================
-- Alexandria National University - Faculty of Engineering
-- Introduction to Database Systems (Fall 2026) - Lab 4
-- File: problem2_DML.sql
-- Students:
--   1. A'laa Sherif Ibrahim (ID: 2304249)
--   2. Mariam Mohamed Ali   (ID: 2304251)
-- ============================================================================

USE library;

-- Authors 1 and 2 are both from UK; author 4 has no books; author 1 wrote 3 books
INSERT INTO author (author_id, name, country, photo_path) VALUES
(1, 'George Orwell',  'UK',    '/static/uploads/authors/author_1.png'),
(2, 'Jane Austen',    'UK',    '/static/uploads/authors/author_2.png'),
(3, 'Naguib Mahfouz', 'Egypt', '/static/uploads/authors/author_3.png'),
(4, 'Emily Writer',   'USA',   '/static/uploads/authors/author_4.png');

-- Publisher 1 is from UK (same as authors 1, 2); publisher 2 from Egypt (same as author 3)
INSERT INTO publisher (publisher_id, name, country) VALUES
(1, 'Penguin Books',  'UK'),
(2, 'Dar El Shorouk', 'Egypt'),
(3, 'Random House',   'USA');

INSERT INTO category (category_id, name) VALUES
(1, 'Fiction'),
(2, 'Classic'),
(3, 'Politics');

-- Book 4 and 9 cost between 15 and 20; book 10 is never borrowed
INSERT INTO book (book_id, title, price, publish_year, author_id, publisher_id, category_id, cover_path) VALUES
(1,  '1984',                  18.50, 1949, 1, 1, 1, '/static/uploads/covers/book_101.png'),
(2,  'Animal Farm',           12.00, 1945, 1, 1, 3, '/static/uploads/covers/book_102.png'),
(3,  'Homage to Catalonia',   22.00, 1938, 1, 3, 3, '/static/uploads/covers/book_103.png'),
(4,  'Pride and Prejudice',   16.00, 1813, 2, 1, 2, '/static/uploads/covers/book_201.png'),
(5,  'Emma',                  14.00, 1815, 2, 1, 2, '/static/uploads/covers/book_202.png'),
(6,  'Palace Walk',           25.00, 1956, 3, 2, 1, '/static/uploads/covers/book_301.png'),
(7,  'Sugar Street',          27.50, 1957, 3, 2, 1, '/static/uploads/covers/book_302.png'),
(8,  'Children of the Alley', 19.00, 1959, 3, 2, 2, '/static/uploads/covers/book_401.png'),
(9,  'Sense and Sensibility', 17.50, 1811, 2, 3, 2, '/static/uploads/covers/book_201.png'),
(10, 'Midnight Tales',        30.00, 2020, 3, 3, 1, '/static/uploads/covers/book_301.png');

INSERT INTO member (member_id, name, email, join_date) VALUES
(1, 'Ali Mostafa', 'ali@example.com',   '2024-01-10'),
(2, 'Nour Ahmed',  'nour@example.com',  '2024-03-05'),
(3, 'Hana Sherif', 'hana@example.com',  '2024-06-20'),
(4, 'Tarek Fouad', 'tarek@example.com', '2025-02-14'),
(5, 'Dina Gamal',  'dina@example.com',  '2025-09-01');   -- Dina has no loans

-- 12 loans; loans 11 and 12 are not returned yet; book 10 never borrowed
INSERT INTO loan (loan_id, book_id, member_id, loan_date, return_date) VALUES
(1,  1, 1, '2025-01-05', '2025-01-20'),
(2,  1, 2, '2025-02-01', '2025-02-15'),
(3,  1, 3, '2025-03-10', '2025-03-25'),
(4,  2, 1, '2025-04-02', '2025-04-16'),
(5,  2, 2, '2025-05-11', '2025-05-30'),
(6,  4, 1, '2025-06-01', '2025-06-14'),
(7,  6, 3, '2025-07-07', '2025-07-21'),
(8,  6, 4, '2025-08-15', '2025-08-29'),
(9,  5, 4, '2025-09-10', '2025-09-24'),
(10, 7, 2, '2025-10-01', '2025-10-12'),
(11, 8, 1, '2026-11-01', NULL),
(12, 3, 3, '2026-11-05', NULL);