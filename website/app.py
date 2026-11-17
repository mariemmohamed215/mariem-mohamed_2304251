import os
import uuid
from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.utils import secure_filename
import mysql.connector

app = Flask(__name__)
app.secret_key = "anu_lab4_secret_key"

DB_CONFIG = {
    "host": os.environ.get("DB_HOST", "localhost"),
    "user": os.environ.get("DB_USER", "root"),
    "password": os.environ.get("DB_PASS", "RootAlaaSql2028"),
    "database": os.environ.get("DB_NAME", "library")
}

UPLOAD_COVERS = os.path.join(app.root_path, "static", "uploads", "covers")
UPLOAD_AUTHORS = os.path.join(app.root_path, "static", "uploads", "authors")
os.makedirs(UPLOAD_COVERS, exist_ok=True)
os.makedirs(UPLOAD_AUTHORS, exist_ok=True)


def get_db_connection():
    return mysql.connector.connect(**DB_CONFIG)


def save_uploaded_image(file_storage, subfolder):
    if file_storage and file_storage.filename:
        ext = os.path.splitext(secure_filename(file_storage.filename))[1].lower()
        filename = f"{uuid.uuid4().hex}{ext}"
        rel_path = f"/static/uploads/{subfolder}/{filename}"
        abs_path = os.path.join(app.root_path, "static", "uploads", subfolder, filename)
        file_storage.save(abs_path)
        return rel_path
    return None


# ============================================================================
# LAB 3 ROUTES (Manage Books & Authors CRUD)
# ============================================================================
@app.route("/")
@app.route("/lab3")
def index():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT author_id, name, country, photo_path FROM author ORDER BY author_id ASC")
    authors = cursor.fetchall()
    cursor.execute("SELECT book_id, title, price, publish_year, author_id, publisher_id, category_id, cover_path FROM book ORDER BY book_id ASC")
    books = cursor.fetchall()
    cursor.execute("SELECT publisher_id, name FROM publisher ORDER BY publisher_id ASC")
    publishers = cursor.fetchall()
    cursor.execute("SELECT category_id, name FROM category ORDER BY category_id ASC")
    categories = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template("index.html", authors=authors, books=books, publishers=publishers, categories=categories)


@app.route("/authors/add", methods=["POST"])
def add_author():
    author_id = request.form.get("author_id")
    name = request.form["name"]
    country = request.form["country"]
    photo_path = save_uploaded_image(request.files.get("photo_file"), "authors")

    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        if author_id:
            cursor.execute(
                "INSERT INTO author (author_id, name, country, photo_path) VALUES (%s, %s, %s, %s)",
                (author_id, name, country, photo_path)
            )
        else:
            cursor.execute(
                "INSERT INTO author (name, country, photo_path) VALUES (%s, %s, %s)",
                (name, country, photo_path)
            )
        conn.commit()
        flash("Author added successfully.", "success")
    except mysql.connector.Error as err:
        flash(f"MySQL Error: {err}", "danger")
    finally:
        cursor.close()
        conn.close()
    return redirect(url_for("index"))


@app.route("/authors/edit", methods=["POST"])
def edit_author():
    author_id = request.form["author_id"]
    name = request.form["name"]
    country = request.form["country"]
    photo_path = save_uploaded_image(request.files.get("photo_file"), "authors")

    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        if photo_path:
            cursor.execute(
                "UPDATE author SET name = %s, country = %s, photo_path = %s WHERE author_id = %s",
                (name, country, photo_path, author_id)
            )
        else:
            cursor.execute(
                "UPDATE author SET name = %s, country = %s WHERE author_id = %s",
                (name, country, author_id)
            )
        conn.commit()
        flash(f"Author #{author_id} updated successfully.", "success")
    except mysql.connector.Error as err:
        flash(f"MySQL Error: {err}", "danger")
    finally:
        cursor.close()
        conn.close()
    return redirect(url_for("index"))


@app.route("/authors/delete/<int:author_id>", methods=["POST"])
def delete_author(author_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM author WHERE author_id = %s", (author_id,))
        conn.commit()
        flash(f"Author #{author_id} and all their books were removed (ON DELETE CASCADE).", "warning")
    except mysql.connector.Error as err:
        flash(f"MySQL Error: {err}", "danger")
    finally:
        cursor.close()
        conn.close()
    return redirect(url_for("index"))


@app.route("/books/add", methods=["POST"])
def add_book():
    book_id = request.form.get("book_id")
    title = request.form["title"]
    price = request.form["price"]
    publish_year = request.form.get("publish_year") or 2020
    author_id = request.form["author_id"]
    publisher_id = request.form.get("publisher_id") or 1
    category_id = request.form.get("category_id") or 1
    cover_path = save_uploaded_image(request.files.get("cover_file"), "covers")

    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        if book_id:
            cursor.execute(
                "INSERT INTO book (book_id, title, price, publish_year, author_id, publisher_id, category_id, cover_path) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                (book_id, title, price, publish_year, author_id, publisher_id, category_id, cover_path)
            )
        else:
            cursor.execute(
                "INSERT INTO book (title, price, publish_year, author_id, publisher_id, category_id, cover_path) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                (title, price, publish_year, author_id, publisher_id, category_id, cover_path)
            )
        conn.commit()
        flash("Book added successfully.", "success")
    except mysql.connector.Error as err:
        flash(f"MySQL Error: {err}", "danger")
    finally:
        cursor.close()
        conn.close()
    return redirect(url_for("index"))


@app.route("/books/edit", methods=["POST"])
def edit_book():
    book_id = request.form["book_id"]
    title = request.form["title"]
    price = request.form["price"]
    author_id = request.form["author_id"]
    cover_path = save_uploaded_image(request.files.get("cover_file"), "covers")

    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        if cover_path:
            cursor.execute(
                "UPDATE book SET title = %s, price = %s, author_id = %s, cover_path = %s WHERE book_id = %s",
                (title, price, author_id, cover_path, book_id)
            )
        else:
            cursor.execute(
                "UPDATE book SET title = %s, price = %s, author_id = %s WHERE book_id = %s",
                (title, price, author_id, book_id)
            )
        conn.commit()
        flash(f"Book #{book_id} updated successfully.", "success")
    except mysql.connector.Error as err:
        flash(f"MySQL Error: {err}", "danger")
    finally:
        cursor.close()
        conn.close()
    return redirect(url_for("index"))


@app.route("/books/delete/<int:book_id>", methods=["POST"])
def delete_book(book_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM book WHERE book_id = %s", (book_id,))
        conn.commit()
        flash(f"Book #{book_id} removed successfully.", "info")
    except mysql.connector.Error as err:
        flash(f"MySQL Error: {err}", "danger")
    finally:
        cursor.close()
        conn.close()
    return redirect(url_for("index"))


# ============================================================================
# LAB 4 ROUTES (F2.1 to F2.6 Search & Analytics Pages)
# ============================================================================

# F2.1 Search books (WHERE + Bonus Prepared Statements)
@app.route("/search", methods=["GET", "POST"])
def search_books():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True, prepared=True)
    cursor.execute("SELECT category_id, name FROM category ORDER BY name")
    categories = cursor.fetchall()

    results = None
    filters = {"title": "", "min_price": "0", "max_price": "100", "category_id": ""}

    if request.method == "POST":
        title_raw = request.form.get("title", "").strip()
        min_price = float(request.form.get("min_price") or 0)
        max_price = float(request.form.get("max_price") or 999999)
        category_id = int(request.form.get("category_id"))

        filters = {
            "title": title_raw,
            "min_price": request.form.get("min_price", "0"),
            "max_price": request.form.get("max_price", "100"),
            "category_id": str(category_id)
        }

        sql = """
            SELECT b.book_id, b.title, b.price, c.name AS category
            FROM book b JOIN category c ON b.category_id = c.category_id
            WHERE b.title LIKE %s AND b.price BETWEEN %s AND %s AND b.category_id = %s
            ORDER BY b.price ASC
        """
        cursor.execute(sql, (f"%{title_raw}%", min_price, max_price, category_id))
        results = cursor.fetchall()

    cursor.close()
    conn.close()
    return render_template("search.html", categories=categories, results=results, filters=filters)


# F2.2 Catalogue (JOIN)
@app.route("/catalogue")
def catalogue():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("""
        SELECT b.book_id, b.title, b.price, b.publish_year,
               a.name AS author, p.name AS publisher, c.name AS category
        FROM book b
        JOIN author a ON b.author_id = a.author_id
        JOIN publisher p ON b.publisher_id = p.publisher_id
        JOIN category c ON b.category_id = c.category_id
        ORDER BY b.title
    """)
    books = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template("catalogue.html", books=books)


# F2.3 Reports (GROUP BY, HAVING)
@app.route("/reports")
def reports():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("""
        SELECT c.name AS category, COUNT(b.book_id) AS books, AVG(b.price) AS average_price
        FROM category c LEFT JOIN book b ON b.category_id = c.category_id
        GROUP BY c.category_id, c.name
    """)
    cat_stats = cursor.fetchall()

    cursor.execute("""
        SELECT a.name AS author, COUNT(b.book_id) AS books
        FROM author a JOIN book b ON b.author_id = a.author_id
        GROUP BY a.author_id, a.name
        HAVING COUNT(b.book_id) >= 2
    """)
    author_stats = cursor.fetchall()

    cursor.execute("""
        SELECT SUM(price) AS total_price, MIN(price) AS smallest_price, MAX(price) AS largest_price
        FROM book
    """)
    lib_stats = cursor.fetchone()

    cursor.close()
    conn.close()
    return render_template("reports.html", cat_stats=cat_stats, author_stats=author_stats, lib_stats=lib_stats)


# F2.4 Loans (JOIN, LEFT JOIN)
@app.route("/loans")
def loans():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("""
        SELECT l.loan_id, b.title, m.name AS member, l.loan_date
        FROM loan l
        JOIN book b ON l.book_id = b.book_id
        JOIN member m ON l.member_id = m.member_id
        WHERE l.return_date IS NULL
    """)
    unreturned = cursor.fetchall()

    cursor.execute("""
        SELECT m.member_id, m.name
        FROM member m LEFT JOIN loan l ON l.member_id = m.member_id
        WHERE l.loan_id IS NULL
    """)
    no_loans = cursor.fetchall()

    cursor.execute("""
        SELECT b.book_id, b.title
        FROM book b LEFT JOIN loan l ON l.book_id = b.book_id
        WHERE l.loan_id IS NULL
    """)
    never_borrowed = cursor.fetchall()

    cursor.close()
    conn.close()
    return render_template("loans.html", unreturned=unreturned, no_loans=no_loans, never_borrowed=never_borrowed)


# F2.5 Most borrowed (GROUP BY, ORDER BY, LIMIT)
@app.route("/most-borrowed")
def most_borrowed():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("""
        SELECT b.title, COUNT(*) AS loans
        FROM book b JOIN loan l ON l.book_id = b.book_id
        GROUP BY b.book_id, b.title
        ORDER BY loans DESC
        LIMIT 3
    """)
    top_books = cursor.fetchall()

    cursor.execute("""
        SELECT m.name, COUNT(*) AS loans
        FROM member m JOIN loan l ON l.member_id = m.member_id
        GROUP BY m.member_id, m.name
        ORDER BY loans DESC
        LIMIT 1
    """)
    top_member = cursor.fetchone()

    cursor.close()
    conn.close()
    return render_template("most_borrowed.html", top_books=top_books, top_member=top_member)


# F2.6 Authors and books (LEFT JOIN, JOIN)
@app.route("/authors")
def authors():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("""
        SELECT a.name AS author, COUNT(b.book_id) AS books
        FROM author a LEFT JOIN book b ON b.author_id = a.author_id
        GROUP BY a.author_id, a.name
    """)
    all_authors = cursor.fetchall()

    cursor.execute("""
        SELECT b.title, a.name AS author, p.name AS publisher, a.country
        FROM book b
        JOIN author a ON b.author_id = a.author_id
        JOIN publisher p ON b.publisher_id = p.publisher_id
        WHERE a.country = p.country
    """)
    same_country = cursor.fetchall()

    cursor.close()
    conn.close()
    return render_template("authors.html", all_authors=all_authors, same_country=same_country)


if __name__ == "__main__":
    app.run(debug=True, port=5000)