import sqlite3
from datetime import datetime

conn = sqlite3.connect('fees.db')
cursor = conn.cursor()

def setup_database():
    cursor.execute('''CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        class TEXT,
        total_fee REAL
    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS fee_records (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_id INTEGER,
        date TEXT,
        amount_paid REAL,
        slip_no TEXT,
        remaining_fee REAL,
        FOREIGN KEY(student_id) REFERENCES students(id)
    )''')
    conn.commit()

def add_student(name, student_class, total_fee):
    cursor.execute("INSERT INTO students (name, class, total_fee) VALUES (?, ?, ?)",
                   (name, student_class, total_fee))
    conn.commit()

def add_fee_record(student_id, amount_paid, slip_no):
    cursor.execute("SELECT total_fee FROM students WHERE id=?", (student_id,))
    result = cursor.fetchone()
    if not result:
        print("Student not found.")
        return

    total_fee = result[0]

    cursor.execute("SELECT SUM(amount_paid) FROM fee_records WHERE student_id=?", (student_id,))
    total_paid = cursor.fetchone()[0] or 0

    remaining = total_fee - total_paid - amount_paid
    date = datetime.today().strftime('%Y-%m-%d')

    cursor.execute('''INSERT INTO fee_records (student_id, date, amount_paid, slip_no, remaining_fee)
                      VALUES (?, ?, ?, ?, ?)''',
                   (student_id, date, amount_paid, slip_no, remaining))
    conn.commit()

def view_student(student_id):
    cursor.execute("SELECT * FROM students WHERE id=?", (student_id,))
    student = cursor.fetchone()
    if not student:
        print("Student not found.")
        return

    print(f"\nStudent: {student[1]} | Class: {student[2]} | Total Fee: {student[3]}")

    cursor.execute("SELECT * FROM fee_records WHERE student_id=?", (student_id,))
    records = cursor.fetchall()
    if records:
        print("Fee Records:")
        for rec in records:
            print(f"  Date: {rec[2]} | Paid: {rec[3]} | Slip No: {rec[4]} | Remaining: {rec[5]}")
    else:
        print("  No fee records found.")


