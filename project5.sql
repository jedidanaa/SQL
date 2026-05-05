DROP TABLE IF EXISTS Enrollments, Students, Courses;

CREATE TABLE Students (
    student_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50),
    email VARCHAR(100) UNIQUE
);

CREATE TABLE Courses (
    course_id INT PRIMARY KEY AUTO_INCREMENT,
    course_name VARCHAR(100),
    credits INT
);

CREATE TABLE Enrollments (
    enrollment_id INT PRIMARY KEY AUTO_INCREMENT,
    student_id INT,
    course_id INT,
    grade DECIMAL(3,2),
    FOREIGN KEY (student_id) REFERENCES Students(student_id),
    FOREIGN KEY (course_id) REFERENCES Courses(course_id)
);

INSERT INTO Students (name, email) VALUES
('Ama Mensah', 'ama@example.com'),
('Kwame Boateng', 'kwame@example.com');

INSERT INTO Courses (course_name, credits) VALUES
('Database Systems', 3),
('Linear Algebra', 4);

INSERT INTO Enrollments (student_id, course_id, grade) VALUES
(1, 1, 3.5),
(2, 2, 4.0);

SELECT s.name
FROM Students s
JOIN Enrollments e ON s.student_id = e.student_id
JOIN Courses c ON e.course_id = c.course_id
WHERE c.course_name = 'Database Systems';

-- Average grade per course
SELECT c.course_name, AVG(e.grade) AS avg_grade
FROM Courses c
JOIN Enrollments e ON c.course_id = e.course_id
GROUP BY c.course_name;
