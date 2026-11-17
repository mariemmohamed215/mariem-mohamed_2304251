# Introduction to Database Systems - Lab 4: Search Queries in SQL & Web Integration

**Alexandria National University - Faculty of Engineering (Fall 2026)**  
**Course Instructor:** Dr. Yasser Fouad  
**Teaching Assistants:** Eng. Abdallah Elsayed, Eng. Basem Hesham, Eng. Danny Hossam

---

## Team Members
| Student Name | Student ID | Academic Role & Contributions |
| :--- | :--- | :--- |
| **A'laa Sherif Ibrahim** | `2304249` | Database Schema Design, DDL/DML Scripting & Flask Backend Integration |
| **Mariam Mohamed Ali** | `2304251` | SQL Query Formulation, Web UI/UX Design & Testing |

---

## Project Overview
This repository contains the complete deliverables for **Lab 4**, which builds upon Lab 3 by expanding relational schemas, enforcing complex referential integrity constraints, executing advanced SQL queries (Aggregation, Joins, Group By, Having, Left Join, Self Join), and upgrading the Flask web application to support advanced search and analytics dashboards.

---

## Repository Deliverables Structure

```text
lab4-2304249-2304251/
├── problem1_DDL.sql          # 5-table COMPANY database schema & foreign keys
├── problem1_DML.sql          # Seed rows for COMPANY satisfying all query test cases
├── problem1_Answers.txt      # Q1.1-Q1.12 SQL scripts, client outputs, errors & explanations
├── problem2_DDL.sql          # 6-table LIBRARY database schema with ON DELETE CASCADE
├── problem2_DML.sql          # Seed data (4 authors, 3 publishers, 3 categories, 10 books, 5 members, 12 loans)
├── problem2_Queries.sql      # Standalone SQL queries for pages F2.1 through F2.6
├── run_lab3.bat              # Automated batch script to initialize databases and start Flask
└── website/                  # Full-stack Python Flask web application
    ├── app.py                # Backend routes for Lab 3 CRUD and Lab 4 analytics
    ├── requirements.txt      # Python dependencies (Flask, mysql-connector-python, etc.)
    ├── static/               # Uploaded book covers and author photos
    └── templates/            # Jinja2 HTML5 & Bootstrap 5 UI templates
        ├── base.html         # Navbar and global layout wrapper
        ├── index.html        # Lab 3 Author & Book Management Dashboard
        ├── search.html       # F2.1 Book Search Engine (with Prepared Statements Bonus)
        ├── catalogue.html    # F2.2 Full Book Catalogue (JOINs)
        ├── reports.html      # F2.3 Category and Author Aggregation Reports
        ├── loans.html        # F2.4 Active Loans and Unborrowed Entities Tracking
        ├── most_borrowed.html# F2.5 Top Borrowed Books & Members Analytics
        └── authors.html      # F2.6 Author Book Counts & Country-Matching Publisher Queries
```

---

## Database Schemas & Architecture

### 1. Part I: The `company` Database (5 Tables)
* **`department`**: `Dnumber` (PK), `Dname`, `mgr_ssn` (FK), `mgr_start_date`
* **`employee`**: `ssn` (PK), `fname`, `lname`, `bdate`, `address`, `gender`, `salary`, `super_ssn` (FK), `Dno` (FK)
* **`project`**: `Pnumber` (PK), `Pname`, `Plocation`, `Dno` (FK)
* **`works_on`**: `essn` (PK/FK), `Pno` (PK/FK), `hours`
* **`dependent`**: `essn` (PK/FK), `dependent_name` (PK), `gender`, `bdate`, `relationship`

### 2. Part II: The `library` Database (6 Tables)
* **`author`**: `author_id` (PK), `name`, `country`, `photo_path`
* **`publisher`**: `publisher_id` (PK), `name`, `country`
* **`category`**: `category_id` (PK), `name`
* **`book`**: `book_id` (PK), `title`, `price`, `publish_year`, `author_id` (FK), `publisher_id` (FK), `category_id` (FK), `cover_path`
* **`member`**: `member_id` (PK), `name`, `email`, `join_date`
* **`loan`**: `loan_id` (PK), `book_id` (FK), `member_id` (FK), `loan_date`, `return_date`

---

## Step-by-Step Instructions to Run

### Prerequisites
* MySQL Server 8.x installed and running.
* Python 3.10+ installed and added to system PATH.

### Method A: Automated One-Click Run (Windows)
Open VS Code terminal in the project root folder and execute:
```powershell
.\run_lab3.bat
```

### Method B: Manual CLI Execution
1. **Initialize and Seed Databases via MySQL CLI:**
   ```bash
   mysql -u root -p < problem1_DDL.sql
   mysql -u root -p < problem1_DML.sql
   mysql -u root -p < problem2_DDL.sql
   mysql -u root -p < problem2_DML.sql
   mysql -u root -p < problem2_Queries.sql
   ```
2. **Launch the Flask Web Application:**
   ```bash
   cd website
   pip install -r requirements.txt
   python app.py
   ```
3. Open your browser and navigate to: **`http://127.0.0.1:5000`**

---

## Web Application Features & Routes
* **`/lab3`**: Lab 3 CRUD interface for managing authors and books with cascading deletes (`ON DELETE CASCADE`) and image uploads.
* **`/search` (F2.1)**: Filter books by title keyword (`LIKE`), price range (`BETWEEN`), and category using secure prepared statements (Bonus).
* **`/catalogue` (F2.2)**: Comprehensive book catalog resolving foreign keys into readable names via multi-table `JOIN` operations.
* **`/reports` (F2.3)**: Statistical reports utilizing `GROUP BY` and `HAVING` clauses (category averages and prolific authors).
* **`/loans` (F2.4)**: Active unreturned loans, members with zero borrowing history, and unborrowed books using `LEFT JOIN`.
* **`/most-borrowed` (F2.5)**: Top 3 most borrowed books and the most active member using `ORDER BY` and `LIMIT`.
* **`/authors` (F2.6)**: Complete author inventory (including those with 0 books) and country-matched author/publisher publishing records.
