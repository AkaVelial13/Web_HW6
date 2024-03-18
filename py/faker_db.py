from faker import Faker
import sqlite3
import random
import datetime
import os


# create Faker object
fake = Faker()

# execute path for work directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# path for db file
db_path = os.path.join(current_dir, '..', 'university.db')

# connection to db
conn = sqlite3.connect(db_path)
cursor = conn.cursor()


# adapter to convert datetime.date objects to strings
def adapt_date(date):
    return date.strftime("%Y-%m-%d")


# register adapter for datetime.date type
sqlite3.register_adapter(datetime.date, adapt_date)


# generate students
for _ in range(50):
    cursor.execute("INSERT INTO students (name, group_id) VALUES (?, ?)",
                   (fake.name(), random.randint(1, 3)))

# generate groups
for group_id in range(1, 4):
    cursor.execute("INSERT INTO groups (id, name) VALUES (?, ?)",
                   (group_id, f"Group {group_id}"))

# generate teachers
for _ in range(5):
    cursor.execute("INSERT INTO teachers (name) VALUES (?)", (fake.name(),))

# generate subjects with random teacher for each
for subject_id in range(1, 9):
    cursor.execute("INSERT INTO subjects (id, name, teacher_id) VALUES (?, ?, ?)",
                   (subject_id, fake.word(), random.randint(1, 5)))

# generate grades for each student for each subject
for student_id in range(1, 51):
    for subject_id in range(1, 9):
        num_grades = random.randint(1, 3)
        for i in range(num_grades):
            score = random.randint(10, 100)
            date_received = fake.date_between(start_date='-1y', end_date='today')
            cursor.execute("INSERT INTO grades (student_id, subject_id, grade, date) VALUES (?, ?, ?, ?)",
                           (student_id, subject_id, score, date_received))

# # save changes to db/ close connection to db
conn.commit()
conn.close()
