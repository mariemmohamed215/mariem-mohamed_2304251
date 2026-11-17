-- ============================================================================
-- Alexandria National University - Faculty of Engineering
-- Introduction to Database Systems (Fall 2026) - Lab 4
-- File: problem2_Queries.sql
-- Students:
--   1. A'laa Sherif Ibrahim (ID: 2304249)
--   2. Mariam Mohamed Ali   (ID: 2304251)
-- ============================================================================

USE library;

-- F2.1 Search books (example values; website uses prepared placeholders)
SELECT b.book_id, b.title, b.price, c.name AS category
FROM book b JOIN category c ON b.category_id = c.category_id
WHERE b.title LIKE '%and%' AND b.price BETWEEN 15 AND 20 AND b.category_id = 2
ORDER BY b.price ASC;

-- F2.2 Catalogue (JOIN)
SELECT b.book_id, b.title, b.price, b.publish_year,
       a.name AS author, p.name AS publisher, c.name AS category
FROM book b
JOIN author a ON b.author_id = a.author_id
JOIN publisher p ON b.publisher_id = p.publisher_id
JOIN category c ON b.category_id = c.category_id
ORDER BY b.title;

-- F2.3(a) Number of books and average price of each category
SELECT c.name AS category, COUNT(b.book_id) AS books, AVG(b.price) AS average_price
FROM category c LEFT JOIN book b ON b.category_id = c.category_id
GROUP BY c.category_id, c.name;

-- F2.3(b) Authors who wrote at least 2 books
SELECT a.name AS author, COUNT(b.book_id) AS books
FROM author a JOIN book b ON b.author_id = a.author_id
GROUP BY a.author_id, a.name
HAVING COUNT(b.book_id) >= 2;

-- F2.3(c) Total, smallest and largest price of the library
SELECT SUM(price) AS total_price, MIN(price) AS smallest_price, MAX(price) AS largest_price
FROM book;

-- F2.4(a) Loans not returned yet
SELECT l.loan_id, b.title, m.name AS member, l.loan_date
FROM loan l JOIN book b ON l.book_id = b.book_id
JOIN member m ON l.member_id = m.member_id
WHERE l.return_date IS NULL;

-- F2.4(b) Members who never borrowed a book
SELECT m.member_id, m.name
FROM member m LEFT JOIN loan l ON l.member_id = m.member_id
WHERE l.loan_id IS NULL;

-- F2.4(c) Books that were never borrowed
SELECT b.book_id, b.title
FROM book b LEFT JOIN loan l ON l.book_id = b.book_id
WHERE l.loan_id IS NULL;

-- F2.5(a) Three books with the most loans
SELECT b.title, COUNT(*) AS loans
FROM book b JOIN loan l ON l.book_id = b.book_id
GROUP BY b.book_id, b.title
ORDER BY loans DESC
LIMIT 3;

-- F2.5(b) Member with the most loans
SELECT m.name, COUNT(*) AS loans
FROM member m JOIN loan l ON l.member_id = m.member_id
GROUP BY m.member_id, m.name
ORDER BY loans DESC
LIMIT 1;

-- F2.6(a) Every author and their number of books, including authors with zero
SELECT a.name AS author, COUNT(b.book_id) AS books
FROM author a LEFT JOIN book b ON b.author_id = a.author_id
GROUP BY a.author_id, a.name;

-- F2.6(b) Books whose author and publisher are from the same country
SELECT b.title, a.name AS author, p.name AS publisher, a.country
FROM book b JOIN author a ON b.author_id = a.author_id
JOIN publisher p ON b.publisher_id = p.publisher_id
WHERE a.country = p.country;