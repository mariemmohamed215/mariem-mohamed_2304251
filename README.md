# Introduction to Database Systems — Lab 4: Search Queries in SQL & Web Integration

**Alexandria National University — Faculty of Engineering (Fall 2026)**  
**Course Instructor:** Dr. Yasser Fouad[cite: 14]  
**Teaching Assistants:** Eng. Abdallah Elsayed, Eng. Basem Hesham, Eng. Danny Hossam[cite: 14]

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
├── problem1_DDL.sql          # 5-table COMPANY database schema & foreign keys[cite: 15, 16]
├── problem1_DML.sql          # Seed rows for COMPANY satisfying all query test cases[cite: 16]
├── problem1_Answers.txt      # Q1.1–Q1.12 SQL scripts, client outputs, errors & explanations[cite: 16]
├── problem2_DDL.sql          # 6-table LIBRARY database schema with ON DELETE CASCADE
├── problem2_DML.sql          # Seed data (4 authors, 3 publishers, 3 categories, 10 books, 5 members, 12 loans)
├── problem2_Queries.sql      # Standalone SQL queries for pages F2.1 through F2.6
├── run_lab4.bat              # Automated batch script to initialize databases and start Flask
└── website/                  # Full-stack Python Flask web application
    ├── app.py                # Backend routes for Lab 3 CRUD and Lab 4 analytics[cite: 9, 17, 18]
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



