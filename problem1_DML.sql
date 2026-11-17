-- ============================================================================
-- Alexandria National University - Faculty of Engineering
-- Introduction to Database Systems (Fall 2026) - Lab 4
-- File: problem1_DML.sql
-- Students:
--   1. A'laa Sherif Ibrahim (ID: 2304249)
--   2. Mariam Mohamed Ali   (ID: 2304251)
-- ============================================================================

USE company;

INSERT INTO department (Dnumber, Dname, mgr_ssn, mgr_start_date) VALUES
(1, 'Research',  NULL, NULL),
(2, 'Sales',     NULL, NULL),
(3, 'Marketing', NULL, NULL);   -- Marketing has no employees

-- 7 employees; Ahmed has no supervisor; Research has 4 employees (> 2)
INSERT INTO employee VALUES
('111111111','Ahmed', 'Hassan', '1980-05-10','12 Cairo Street, Cairo',       'M', 8000, NULL,       1),
('222222222','Mona',  'Samir',  '1985-03-22','5 Nile Road, Giza',            'F', 5500, '111111111',1),
('333333333','Omar',  'Khaled', '1990-07-15','8 Corniche, Alexandria',       'M', 4200, '222222222',1),
('444444444','Salma', 'Nabil',  '1992-11-02','3 Port Said St, Alexandria',   'F', 2800, '222222222',1),
('555555555','Youssef','Adel',  '1983-01-30','20 Tahrir Square, Cairo',      'M', 6500, '111111111',2),
('666666666','Laila', 'Fathy',  '1995-09-09','9 Mansoura Road, Mansoura',    'F', 3100, '555555555',2),
('777777777','Karim', 'Zaki',   '1988-12-12','14 Stanley, Alexandria',       'M', 3600, '555555555',2);

UPDATE department SET mgr_ssn='222222222', mgr_start_date='2015-01-01' WHERE Dnumber=1;
UPDATE department SET mgr_ssn='555555555', mgr_start_date='2018-06-01' WHERE Dnumber=2;

-- Project 4 has nobody working on it
INSERT INTO project VALUES
(1, 'ProductX', 'Cairo',      1),
(2, 'ProductY', 'Alexandria', 1),
(3, 'Campaign', 'Cairo',      2),
(4, 'Archive',  'Giza',       2);

-- Omar (333333333) works on two projects
INSERT INTO works_on VALUES
('111111111',1,12.5),
('222222222',1,15.0),
('333333333',1,10.0),
('333333333',2,20.0),
('444444444',2,8.0),
('555555555',3,18.5),
('666666666',3,10.0),
('777777777',3,7.5);

INSERT INTO dependent VALUES
('111111111','Sara',  'F','2010-04-04','Daughter'),
('222222222','Tamer', 'M','2012-08-19','Son'),
('555555555','Nadia', 'F','1984-02-02','Spouse');