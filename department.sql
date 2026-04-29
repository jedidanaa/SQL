DROP TABLE IF  EXISTS DEPARTMENT;
CREATE TABLE IF NOT EXISTS DEPARTMENT (
    EMPLOYEE_ID TEXT,
    NAME TEXT,
    DEPARTMENT_ID TEXT,
    MANAGER_ID TEXT,
    SALARY REAL

);

INSERT INTO DEPARTMENT(EMPLOYEE, NAME, DEPARTMENT, MANAGER, SALARY) VALUES
('100', 'STEVEN KING', '90', '100', 24000),
('101', 'NEENA KOCHCAR', '90', '100', 17000),
('102', 'LEX DEEHAN',  '102',9000),
('103', 'BRUCE LEE', '60', '103', 4000);


SELECT department_id AS "Department Code",

COUNT(*) AS "No of Employees"

FROM DEPARTMENT

GROUP BY department_id;

-- Query to sum the salary of each department

SELECT department_id, SUM(salary)

FROM DEPARTMENT

GROUP BY department_id;

-- Query to count the number of employees and sum the salary in each department

SELECT department_id AS "Department Code",

COUNT(*) AS "No of Employees",

SUM(salary) AS "Total Salary"

FROM DEPARTMENT

GROUP BY department_id;

-- Query to sum the salary of employees with a specific manager

SELECT department_id AS "Department Code",

SUM(salary) AS "Total Salary"

FROM DEPARTMENT

WHERE MANAGER_ID = '103'

GROUP BY department_id;

-- Query to find departments with more than 2 employees

SELECT department_id, COUNT(*) AS "No. of Employees"

FROM DEPARTMENT

GROUP BY department_id

HAVING COUNT(*) > 2;