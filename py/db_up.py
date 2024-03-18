import sqlite3
import os


# execute path for work directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# path for db file
db_path = os.path.join(current_dir, '..', 'university.db')

# connection to db
conn = sqlite3.connect(db_path)

# create cursor for SQL query
cursor = conn.cursor()

# create students table
cursor.execute('''CREATE TABLE IF NOT EXISTS students (
                    id INTEGER PRIMARY KEY,
                    name TEXT,
                    group_id INTEGER,
                    FOREIGN KEY(group_id) REFERENCES groups(id)
                )''')

# create groups table
cursor.execute('''CREATE TABLE IF NOT EXISTS groups (
                    id INTEGER PRIMARY KEY,
                    name TEXT
                )''')

# create teachers table
cursor.execute('''CREATE TABLE IF NOT EXISTS teachers (
                    id INTEGER PRIMARY KEY,
                    name TEXT
                )''')

# create subjects table
cursor.execute('''CREATE TABLE IF NOT EXISTS subjects (
                    id INTEGER PRIMARY KEY,
                    name TEXT,
                    teacher_id INTEGER,
                    FOREIGN KEY(teacher_id) REFERENCES teachers(id)
                )''')

# create students grades table
cursor.execute('''CREATE TABLE IF NOT EXISTS grades (
                    id INTEGER PRIMARY KEY,
                    student_id INTEGER,
                    subject_id INTEGER,
                    grade INTEGER,
                    date TEXT,
                    FOREIGN KEY(student_id) REFERENCES students(id),
                    FOREIGN KEY(subject_id) REFERENCES subjects(id)
                )''')

# save changes to db/ close connection to db
conn.commit()
conn.close()

print("Database and tables created successfully!")
