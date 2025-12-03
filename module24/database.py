import sqlite3

connection = sqlite3.connect('example.db')

cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTs employees (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT not null,
    position INTEGER not null,
    departament TEXT NOT null,
    salary REAL,
''')

connection.commit()
cursor.execute('''
INSERT INTO employees (name, position, departament, salary)
VALUES (?, ?, ?, ?)
''', ('John Doe', 'Software Engineer', 'IT', '2000'))

connection.commit()

cursor.execute('Select * from employees')
rows = cursor.fetchall()
for row in rows:
    print(row)

cursor.execute('''
UPDATE employees
SET salary=?
WHERE name=?
''', (3000, 'John Doe'))

connection.commit()

cursor.close()
connection.close()