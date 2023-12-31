CREATE TABLE students (
    student_id INT PRIMARY KEY NOT NULL,
    student_name VARCHAR(50) NOT NULL,
    date_of_birth DATE NOT NULL,
    is_deleted BOOLEAN);

CREATE TABLE departments (
    department_id INT PRIMARY KEY NOT NULL,
    department_name VARCHAR(100) NOT NULL,
    is_deleted BOOLEAN);

CREATE TABLE instructors(
        instructor_id INT PRIMARY KEY NOT NULL,
        instructor_name VARCHAR(50) NOT NULL,
        specialization VARCHAR(100) NOT NULL,
        department_id BIGINT NOT NULL UNIQUE,
        is_deleted BOOLEAN,
        FOREIGN KEY (department_id) REFERENCES departments(department_id));


CREATE TABLE courses (
    course_id INT PRIMARY KEY NOT NULL,
    title VARCHAR(100) NOT NULL,
    credits INT NOT NULL,
    prerequisites_of_id BIGINT NOT NULL UNIQUE,
    is_prerequisites BOOLEAN,
    instructor_id bigint NOT NULL UNIQUE,
    is_deleted BOOLEAN,
    FOREIGN KEY (prerequisites_of_id) REFERENCES courses(course_id),
    FOREIGN KEY (instructor_id) REFERENCES instructors(instructor_id));


CREATE TABLE StudentRegistration(
       registration_id INT PRIMARY KEY NOT NULL,
       student_id INT NOT NULL UNIQUE,
       course_id INT NOT NULL UNIQUE,
       FOREIGN KEY (student_id) REFERENCES students(student_id),
       FOREIGN KEY (course_id) REFERENCES courses(course_id));

--part e
INSERT INTO students (student_id,student_name,date_of_birth,is_deleted)
VALUES (1, 'Farzam', '1992-08-14', false),
        (2,'Mohammad','1999-07-30',false),
        (3, 'Hossein','2001-04-16',false),
        (4,'Mehdi','1997-10-15',false);

--part f
DELETE FROM students WHERE student_name = 'Mohammad';

UPDATE students SET student_name='Feri'
WHERE student_name='Farzam';

--part g
ALTER TABLE students
ADD phone INT;

DROP TABLE students;

ALTER TABLE students
RENAME TO fake_students;