import sqlite3

# Задача 4.1.
# Домашнее задание на SQL

con = sqlite3.connect("teachers.db")
cur = con.cursor()

# В базе данных teacher создайте таблицу Students
# Структура таблицы: Student_Id - Integer, Student_Name - Text, School_Id - Integer (Primary key)

cur.execute("""
CREATE TABLE IF NOT EXISTS Students (
Student_Id INTEGER NOT NULL PRIMARY KEY,
Student_Name TEXT NOT NULL,
School_Id INTEGER NOT NULL
);
""")

# Наполните таблицу следующими данными:

# 201, Иван, 1
cur.execute("INSERT INTO Students (Student_Id, Student_Name, School_Id) VALUES (201, 'Иван', 1);")
# 202, Петр, 2
cur.execute("INSERT INTO Students (Student_Id, Student_Name, School_Id) VALUES (202, 'Петр', 2);")
# 203, Анастасия, 3
cur.execute("INSERT INTO Students (Student_Id, Student_Name, School_Id) VALUES (203, 'Анастасия', 3);")
# 204, Игорь, 4
cur.execute("INSERT INTO Students (Student_Id, Student_Name, School_Id) VALUES (204, 'Игорь', 4);")

# Напишите программу, с помощью которой по ID студента можно получать информацию о школе и студенте.

student_id = input("Пришлите id студента: ")
student = cur.execute("SELECT * FROM Students WHERE Student_Id=" + student_id).fetchone()
school = cur.execute("SELECT * FROM School WHERE School_Id=" + str(student[2])).fetchone()

# Формат вывода:
# ID Студента:
print("ID Студента:", student[0])
# Имя студента:
print("Имя студента:", student[1])
# ID школы:
print("ID школы:", student[2])
# Название школы:
print("Название школы:", school[1])
