-- LAB 3 - Problem 2: Seed data (at least 3 authors and 6 books)
USE library_lab3;

INSERT INTO author (author_id, name, country) VALUES
(1, 'George Orwell', 'UK'),
(2, 'Jane Austen', 'UK'),
(3, 'Naguib Mahfouz', 'Egypt');

INSERT INTO book (book_id, title, price, author_id) VALUES
(1, '1984', 18.50, 1),
(2, 'Animal Farm', 12.00, 1),
(3, 'Pride and Prejudice', 16.00, 2),
(4, 'Emma', 14.00, 2),
(5, 'Palace Walk', 25.00, 3),
(6, 'Sugar Street', 27.50, 3);
