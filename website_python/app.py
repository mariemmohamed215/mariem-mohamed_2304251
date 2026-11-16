import os
from decimal import Decimal, InvalidOperation

import mysql.connector
from flask import Flask, flash, redirect, render_template, request, url_for

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "change-this-development-secret")

# Database connection settings.
# Set DB_USER, DB_PASS and DB_HOST in your environment if needed.
DB = {
    "host": os.getenv("DB_HOST", "127.0.0.1"),
    "user": os.getenv("DB_USER", "root"),
    "password": os.getenv("DB_PASS", ""),
    "database": "library",
}


def get_connection():
    """Open a connection to the Lab 4 library database."""
    return mysql.connector.connect(**DB)


def fetch_all(sql, params=()):
    """Run a SELECT query and return its rows as dictionaries."""
    connection = get_connection()
    try:
        cursor = connection.cursor(dictionary=True)
        cursor.execute(sql, params)
        return cursor.fetchall()
    finally:
        cursor.close()
        connection.close()


def execute_change(sql, params=()):
    """Run INSERT, UPDATE or DELETE and save the change."""
    connection = get_connection()
    try:
        cursor = connection.cursor()
        cursor.execute(sql, params)
        connection.commit()
        return cursor.lastrowid
    except Exception:
        connection.rollback()
        raise
    finally:
        cursor.close()
        connection.close()


def render_page(title, **context):
    """Render a page using the shared website layout."""
    return render_template("page.html", title=title, **context)


# ---------------------------------------------------------------------
# HOME
# ---------------------------------------------------------------------
@app.route("/")
def home():
    return render_page("Library Management Website", home=True)


# ---------------------------------------------------------------------
# LAB 3 - F2.1: DISPLAY BOOKS AND AUTHORS
# ---------------------------------------------------------------------
@app.route("/lab3")
def lab3_home():
    books = fetch_all("""
        SELECT book_id, title, price, author_id
        FROM book
        ORDER BY book_id
    """)
    authors = fetch_all("""
        SELECT author_id, name, country
        FROM author
        ORDER BY author_id
    """)
    return render_page("Books and Authors",
                       tables=[("Books", books), ("Authors", authors)])


# ---------------------------------------------------------------------
# LAB 3 - F2.2: ADD AN AUTHOR
# ---------------------------------------------------------------------
@app.route("/lab3/authors/add", methods=["GET", "POST"])
def add_author():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        country = request.form.get("country", "").strip()
        if not name:
            flash("Author name is required.", "error")
        else:
            execute_change(
                "INSERT INTO author (name, country) VALUES (%s, %s)",
                (name, country or None)
            )
            flash("Author added successfully.", "success")
            return redirect(url_for("lab3_home"))
    return render_page("Add Author", form_type="author")


# ---------------------------------------------------------------------
# LAB 3 - F2.2: ADD A BOOK
# ---------------------------------------------------------------------
@app.route("/lab3/books/add", methods=["GET", "POST"])
def add_book():
    authors = fetch_all("SELECT author_id, name FROM author ORDER BY name")
    publishers = fetch_all("SELECT publisher_id, name FROM publisher ORDER BY name")
    categories = fetch_all("SELECT category_id, name FROM category ORDER BY name")

    if request.method == "POST":
        try:
            title = request.form.get("title", "").strip()
            price = Decimal(request.form.get("price", ""))
            author_id = int(request.form.get("author_id", ""))
            publisher_id = int(request.form.get("publisher_id", ""))
            category_id = int(request.form.get("category_id", ""))
            year_text = request.form.get("publish_year", "").strip()
            publish_year = int(year_text) if year_text else None

            if not title or price < 0:
                raise ValueError("Enter a title and a non-negative price.")

            execute_change("""
                INSERT INTO book
                    (title, price, publish_year, author_id, publisher_id, category_id)
                VALUES (%s, %s, %s, %s, %s, %s)
            """, (title, price, publish_year, author_id, publisher_id, category_id))
            flash("Book added successfully.", "success")
            return redirect(url_for("lab3_home"))
        except (ValueError, InvalidOperation):
            flash("Please enter valid book details.", "error")

    return render_page("Add Book", form_type="book",
                       authors=authors, publishers=publishers, categories=categories)


# ---------------------------------------------------------------------
# LAB 3 - F2.3: EDIT AN AUTHOR
# ---------------------------------------------------------------------
@app.route("/lab3/authors/edit/<int:author_id>", methods=["GET", "POST"])
def edit_author(author_id):
    author = fetch_all(
        "SELECT author_id, name, country FROM author WHERE author_id = %s",
        (author_id,)
    )
    if not author:
        flash("Author was not found.", "error")
        return redirect(url_for("lab3_home"))

    if request.method == "POST":
        name = request.form.get("name", "").strip()
        country = request.form.get("country", "").strip()
        if not name:
            flash("Author name is required.", "error")
        else:
            execute_change(
                "UPDATE author SET name = %s, country = %s WHERE author_id = %s",
                (name, country or None, author_id)
            )
            flash("Author updated successfully.", "success")
            return redirect(url_for("lab3_home"))

    return render_page("Edit Author", form_type="author",
                       item=author[0])


# ---------------------------------------------------------------------
# LAB 3 - F2.3: EDIT A BOOK
# ---------------------------------------------------------------------
@app.route("/lab3/books/edit/<int:book_id>", methods=["GET", "POST"])
def edit_book(book_id):
    book_rows = fetch_all("SELECT * FROM book WHERE book_id = %s", (book_id,))
    if not book_rows:
        flash("Book was not found.", "error")
        return redirect(url_for("lab3_home"))

    authors = fetch_all("SELECT author_id, name FROM author ORDER BY name")
    publishers = fetch_all("SELECT publisher_id, name FROM publisher ORDER BY name")
    categories = fetch_all("SELECT category_id, name FROM category ORDER BY name")

    if request.method == "POST":
        try:
            title = request.form.get("title", "").strip()
            price = Decimal(request.form.get("price", ""))
            author_id = int(request.form.get("author_id", ""))
            publisher_id = int(request.form.get("publisher_id", ""))
            category_id = int(request.form.get("category_id", ""))
            year_text = request.form.get("publish_year", "").strip()
            publish_year = int(year_text) if year_text else None

            if not title or price < 0:
                raise ValueError("Enter a title and a non-negative price.")

            execute_change("""
                UPDATE book
                SET title=%s, price=%s, publish_year=%s,
                    author_id=%s, publisher_id=%s, category_id=%s
                WHERE book_id=%s
            """, (title, price, publish_year, author_id, publisher_id,
                  category_id, book_id))
            flash("Book updated successfully.", "success")
            return redirect(url_for("lab3_home"))
        except (ValueError, InvalidOperation):
            flash("Please enter valid book details.", "error")

    return render_page("Edit Book", form_type="book",
                       item=book_rows[0], authors=authors,
                       publishers=publishers, categories=categories)


# ---------------------------------------------------------------------
# LAB 3 - F2.4: REMOVE A BOOK
# ---------------------------------------------------------------------
@app.route("/lab3/books/delete/<int:book_id>", methods=["POST"])
def delete_book(book_id):
    execute_change("DELETE FROM book WHERE book_id = %s", (book_id,))
    flash("Book deleted. Its loans are also deleted by ON DELETE CASCADE.", "success")
    return redirect(url_for("lab3_home"))


# ---------------------------------------------------------------------
# LAB 3 - F2.5: REMOVE AN AUTHOR
# ---------------------------------------------------------------------
@app.route("/lab3/authors/delete/<int:author_id>", methods=["POST"])
def delete_author(author_id):
    execute_change("DELETE FROM author WHERE author_id = %s", (author_id,))
    flash("Author deleted. That author's books and their loans are deleted by ON DELETE CASCADE.", "success")
    return redirect(url_for("lab3_home"))


# ---------------------------------------------------------------------
# LAB 4 - F2.1: SEARCH BOOKS (LIKE, BETWEEN, CATEGORY, ORDER BY)
# ---------------------------------------------------------------------
@app.route("/search", methods=["GET"])
def search_books():
    categories = fetch_all("SELECT category_id, name FROM category ORDER BY name")
    keyword = request.args.get("q", "").strip()
    minimum = request.args.get("min", "").strip()
    maximum = request.args.get("max", "").strip()
    category_id = request.args.get("category", "").strip()
    results = []

    if request.args:
        try:
            min_price = Decimal(minimum) if minimum else Decimal("0")
            max_price = Decimal(maximum) if maximum else Decimal("999999")
            if min_price > max_price:
                raise ValueError
            sql = """
                SELECT b.book_id, b.title, b.price, c.name AS category
                FROM book b
                JOIN category c ON b.category_id = c.category_id
                WHERE b.title LIKE %s
                  AND b.price BETWEEN %s AND %s
                  AND (%s = '' OR b.category_id = %s)
                ORDER BY b.price ASC
            """
            results = fetch_all(sql, (
                f"%{keyword}%", min_price, max_price,
                category_id, int(category_id) if category_id else 0
            ))
        except (ValueError, InvalidOperation):
            flash("Please enter a valid price range.", "error")

    return render_page("Search Books", search=True,
                       categories=categories, results=results,
                       q=keyword, minimum=minimum, maximum=maximum,
                       selected_category=category_id)


# ---------------------------------------------------------------------
# LAB 4 - F2.2: CATALOGUE (JOIN)
# ---------------------------------------------------------------------
@app.route("/catalogue")
def catalogue():
    rows = fetch_all("""
        SELECT b.book_id, b.title, b.price, b.publish_year,
               a.name AS author, p.name AS publisher, c.name AS category
        FROM book b
        JOIN author a ON b.author_id = a.author_id
        JOIN publisher p ON b.publisher_id = p.publisher_id
        JOIN category c ON b.category_id = c.category_id
        ORDER BY b.title
    """)
    return render_page("Catalogue", tables=[("All books", rows)])


# ---------------------------------------------------------------------
# LAB 4 - F2.3: REPORTS (GROUP BY, HAVING, AGGREGATES)
# ---------------------------------------------------------------------
@app.route("/reports")
def reports():
    category_report = fetch_all("""
        SELECT c.name AS category, COUNT(b.book_id) AS books,
               ROUND(AVG(b.price), 2) AS average_price
        FROM category c
        LEFT JOIN book b ON b.category_id = c.category_id
        GROUP BY c.category_id, c.name
        ORDER BY c.name
    """)
    authors_report = fetch_all("""
        SELECT a.name AS author, COUNT(b.book_id) AS books
        FROM author a
        JOIN book b ON b.author_id = a.author_id
        GROUP BY a.author_id, a.name
        HAVING COUNT(b.book_id) >= 2
    """)
    prices_report = fetch_all("""
        SELECT ROUND(SUM(price), 2) AS total_price,
               MIN(price) AS smallest_price,
               MAX(price) AS largest_price
        FROM book
    """)
    return render_page("Reports",
        tables=[("Books and average price per category", category_report),
                ("Authors with at least 2 books", authors_report),
                ("Prices of the whole library", prices_report)])


# ---------------------------------------------------------------------
# LAB 4 - F2.4: LOANS (JOIN AND LEFT JOIN)
# ---------------------------------------------------------------------
@app.route("/loans")
def loans():
    active = fetch_all("""
        SELECT l.loan_id, b.title, m.name AS member, l.loan_date
        FROM loan l
        JOIN book b ON l.book_id = b.book_id
        JOIN member m ON l.member_id = m.member_id
        WHERE l.return_date IS NULL
        ORDER BY l.loan_date
    """)
    members_without_loans = fetch_all("""
        SELECT m.member_id, m.name
        FROM member m
        LEFT JOIN loan l ON l.member_id = m.member_id
        WHERE l.loan_id IS NULL
    """)
    books_without_loans = fetch_all("""
        SELECT b.book_id, b.title
        FROM book b
        LEFT JOIN loan l ON l.book_id = b.book_id
        WHERE l.loan_id IS NULL
    """)
    return render_page("Loans",
        tables=[("Loans not returned yet", active),
                ("Members who never borrowed a book", members_without_loans),
                ("Books that were never borrowed", books_without_loans)])


# ---------------------------------------------------------------------
# LAB 4 - F2.5: MOST BORROWED (GROUP BY, ORDER BY, LIMIT)
# ---------------------------------------------------------------------
@app.route("/most-borrowed")
def most_borrowed():
    books = fetch_all("""
        SELECT b.title, COUNT(*) AS loans
        FROM book b
        JOIN loan l ON l.book_id = b.book_id
        GROUP BY b.book_id, b.title
        ORDER BY loans DESC
        LIMIT 3
    """)
    members = fetch_all("""
        SELECT m.name, COUNT(*) AS loans
        FROM member m
        JOIN loan l ON l.member_id = m.member_id
        GROUP BY m.member_id, m.name
        ORDER BY loans DESC
        LIMIT 1
    """)
    return render_page("Most Borrowed",
        tables=[("The 3 most borrowed books", books),
                ("Member with the most loans", members)])


# ---------------------------------------------------------------------
# LAB 4 - F2.6: AUTHORS AND BOOKS (LEFT JOIN AND JOIN)
# ---------------------------------------------------------------------
@app.route("/authors")
def authors():
    counts = fetch_all("""
        SELECT a.author_id, a.name AS author, COUNT(b.book_id) AS books
        FROM author a
        LEFT JOIN book b ON b.author_id = a.author_id
        GROUP BY a.author_id, a.name
        ORDER BY a.name
    """)
    same_country = fetch_all("""
        SELECT b.title, a.name AS author, p.name AS publisher,
               a.country AS country
        FROM book b
        JOIN author a ON b.author_id = a.author_id
        JOIN publisher p ON b.publisher_id = p.publisher_id
        WHERE a.country = p.country
    """)
    return render_page("Authors and Books",
        tables=[("Every author and number of books (including zero)", counts),
                ("Books whose author and publisher share a country", same_country)])


if __name__ == "__main__":
    app.run(debug=True, port=5000)
