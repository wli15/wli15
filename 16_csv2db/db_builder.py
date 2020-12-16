# Team MadCauseBad - Ryan Ma, Jessica Yeung, May Hathaway, William Li
# SoftDev
#K16 -- No Trouble - using SQLite 
#2020-12-16

import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O

DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops -- you will use cursor to trigger db events

#==========================================================

def insert_students_data(name, age, id):
    insert = "INSERT INTO students (name, age, id) VALUES (?, ?, ?);" # ? dictate where input parameters are placed
    data = (name, age, id)
    c.execute(insert, data) # executing a string and a tuple places values of the tuple into ?s in left to right order

c.execute("CREATE TABLE IF NOT EXISTS students (name TEXT, age INTEGER, id INTEGER PRIMARY KEY)")

with open("students.csv", "r") as csv_students:
    students_reader = csv.DictReader(csv_students)
    for row in students_reader:
        insert_students_data(row["name"], row["age"], row["id"])

csv_students.close()

def insert_courses_data(code, mark, id, i): # 4th parameter i such that identical id values dont conflict
    insert = "INSERT INTO courses (code, mark, id, _id) VALUES (?, ?, ?, ?);"
    data = (code, mark, id, i)
    c.execute(insert, data)

c.execute("CREATE TABLE IF NOT EXISTS courses (code TEXT, mark INTEGER, id INTEGER, _id INTEGER PRIMARY KEY )")

with open("courses.csv", "r") as csv_courses:
    courses_reader = csv.DictReader(csv_courses)
    i = 0
    for row in courses_reader:
        insert_courses_data(row["code"], row["mark"], row["id"], i)
        i += 1

csv_courses.close()

#==========================================================

print("Students Database")
students_db = c.execute("SELECT * FROM students")
for row in students_db:
    print(row)

print("<------------------------------------------>")

print("Courses Database")
courses_db = c.execute("SELECT * FROM courses")
for row in courses_db:
    print(row)

db.commit() #save changes
db.close()  #close database