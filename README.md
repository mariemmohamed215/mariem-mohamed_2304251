# Combined Lab 3 + Lab 4 – Library Website

This folder contains the Lab 3 library requirements and the Lab 4 requirements.
The website is implemented **only in Python (Flask)**. PHP is not needed and has
been removed because Flask handles the website routes, forms and database work.

## Folder contents

- `lab3_problem2_DDL.sql` – Lab 3's original two-table library schema, in a separate database named `library_lab3`.
- `lab3_problem2_DML.sql` – Lab 3 seed data (3 authors and 6 books).
- `problem1_DDL.sql` – Lab 4 Problem 1: the `company` database schema.
- `problem1_DML.sql` – Lab 4 Problem 1 seed data for all five tables.
- `problem1_Answers.txt` – Lab 4 Problem 1 answers Q1.1–Q1.12.
- `problem2_DDL.sql` – Lab 4 Problem 2: the expanded six-table `library` schema.
- `problem2_DML.sql` – Lab 4 seed data (4 authors, 3 publishers, 3 categories, 10 books, 5 members, 12 loans).
- `problem2_Queries.sql` – SQL queries for Lab 4 website pages F2.1–F2.6.
- `website_python/` – One combined website for Lab 3 and Lab 4.

The combined website uses the **Lab 4 six-table `library` database**. This database
contains all Lab 3 book/author fields plus the additional publisher, category,
publish-year, member and loan fields. Lab 3's standalone two-table schema is kept
in its own `library_lab3` database so it does not conflict with the expanded Lab 4 schema.

## 1. Requirements

Install:
- MySQL Server and MySQL command-line client
- Python 3.10 or newer

## 2. Create and fill the Lab 4 databases

Open a terminal in this folder and run the following commands. Replace `root`
with your MySQL username if it is different.

```bash
mysql -u root -p < problem1_DDL.sql
mysql -u root -p < problem1_DML.sql

mysql -u root -p < problem2_DDL.sql
mysql -u root -p < problem2_DML.sql
```

Optional: run the Lab 4 search-query script in the MySQL client:

```bash
mysql -u root -p < problem2_Queries.sql
```

## 3. (Optional) Run the original Lab 3 two-table scripts

These create a separate database and do not affect the Lab 4 website:

```bash
mysql -u root -p < lab3_problem2_DDL.sql
mysql -u root -p < lab3_problem2_DML.sql
```

## 4. Configure and run the Python website

Open a terminal and enter the Python website folder:

```bash
cd website_python
python -m venv venv
```

Activate the virtual environment:

Windows:
```bash
venv\Scripts\activate
```

macOS/Linux:
```bash
source venv/bin/activate
```

Install packages:

```bash
pip install -r requirements.txt
```

Set your MySQL password before running the app (Windows PowerShell example):

```powershell
$env:DB_USER="root"
$env:DB_PASS="YOUR_MYSQL_PASSWORD"
$env:DB_HOST="127.0.0.1"
```

macOS/Linux example:

```bash
export DB_USER="root"
export DB_PASS="YOUR_MYSQL_PASSWORD"
export DB_HOST="127.0.0.1"
```

If your MySQL root account has no password, set `DB_PASS` to an empty string
or leave it unset.

Run:

```bash
python app.py
```

Open this address in your browser:

http://127.0.0.1:5000

## 5. Website pages

### Lab 3 – Manage books and authors
- `/lab3` – Display books and authors, with Edit and Delete actions.
- `/lab3/books/add` – Add a book.
- `/lab3/authors/add` – Add an author.
- Edit links appear in the Lab 3 tables.
- Delete actions are provided for books and authors.
- Deleting an author cascades to that author's books; deleting a book cascades to its loans.

### Lab 4 – Search and reports
- `/search` – F2.1 Search books by title keyword, minimum/maximum price and category. Uses parameterized queries (prepared-statement style).
- `/catalogue` – F2.2 Catalogue with author, publisher and category names.
- `/reports` – F2.3 Category counts/average prices, authors with at least two books, and overall price statistics.
- `/loans` – F2.4 Unreturned loans, members with no loans, and books never borrowed.
- `/most-borrowed` – F2.5 Three most borrowed books and member with most loans.
- `/authors` – F2.6 Author book counts (including zero) and books whose author/publisher share a country.

## Notes

- SQL statements are kept in Python for database operations, but **the website does not display the SQL code** under its tables.
- The Lab 4 SQL for each search/report page is also saved in `problem2_Queries.sql`, as required by the handout.
- PHP files were removed because the Flask website implements the same website functionality.
- The Lab 4 six-table library schema is the database to load before opening the combined website.
