-- ============================================================================
-- Alexandria National University - Faculty of Engineering
-- Introduction to Database Systems (Fall 2026) - Lab 4
-- File: problem1_DDL.sql
-- Students:
--   1. A'laa Sherif Ibrahim (ID: 2304249)
--   2. Mariam Mohamed Ali   (ID: 2304251)
-- ============================================================================

DROP DATABASE IF EXISTS company;
CREATE DATABASE company;
USE company;

CREATE TABLE department (
  Dnumber        INT PRIMARY KEY,
  Dname          VARCHAR(40) NOT NULL UNIQUE,
  mgr_ssn        CHAR(9) NULL,
  mgr_start_date DATE
);

CREATE TABLE employee (
  ssn       CHAR(9) PRIMARY KEY,
  fname     VARCHAR(30) NOT NULL,
  lname     VARCHAR(30) NOT NULL,
  bdate     DATE,
  address   VARCHAR(100),
  gender    CHAR(1),
  salary    DECIMAL(10,2),
  super_ssn CHAR(9) NULL,
  Dno       INT,
  FOREIGN KEY (super_ssn) REFERENCES employee(ssn),
  FOREIGN KEY (Dno) REFERENCES department(Dnumber)
);

ALTER TABLE department
  ADD FOREIGN KEY (mgr_ssn) REFERENCES employee(ssn);

CREATE TABLE project (
  Pnumber   INT PRIMARY KEY,
  Pname     VARCHAR(40) NOT NULL,
  Plocation VARCHAR(40),
  Dno       INT NOT NULL,
  FOREIGN KEY (Dno) REFERENCES department(Dnumber)
);

CREATE TABLE works_on (
  essn  CHAR(9),
  Pno   INT,
  hours DECIMAL(5,1),
  PRIMARY KEY (essn, Pno),
  FOREIGN KEY (essn) REFERENCES employee(ssn),
  FOREIGN KEY (Pno)  REFERENCES project(Pnumber)
);

CREATE TABLE dependent (
  essn           CHAR(9),
  dependent_name VARCHAR(40),
  gender         CHAR(1),
  bdate          DATE,
  relationship   VARCHAR(20),
  PRIMARY KEY (essn, dependent_name),
  FOREIGN KEY (essn) REFERENCES employee(ssn)
);