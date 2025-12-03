import sqlite3
con = sqlite3.connect('example.db')
cursor = con.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS students 
    student_id INTEGER PRIMARY KEY ,
    name TEXT, 
)
''')

cursor.execute("INSERT INTO students (name) VALUES ('Alice')")
cursor.execute("INSERT INTO students (name) VALUES ('Bob')")

cursor.execute('''
CREATE TABLE IF NOT EXISTS courses 
course_id INTEGER PRIMARY KEY ,
course_name TEXT, 
student_id INTEGER, 
FOREIGN KEY(student_id) REFERENCES students(student_id)
)
''')

cursor.execute("INSERT INTO courses (course_name, student_id) VALUES (MATH, 1)")
cursor.execute("INSERT INTO courses (course_name, student_id) VALUES (Science, 1)")
cursor.execute("INSERT INTO courses (course_name, student_id) VALUES (Art, 2)")

conn.commit()

cursor.execute('''
SELECT student.name, coursors.course_name
FROM students
JOIN courses ON students.course_id = courses.course_id

''')

rows = cursor.fetchall()
for row in rows:
    print(f"Student: {row[0]}, Courses: {row[1]}")

conn.close()

