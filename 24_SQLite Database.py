import os
import sqlite3
from faker import Faker

# 1
# Database Data Types:
# INT, FLOAT, CHAR, VARCHAR, DATE, TIME, JSON, ENUM, DECIMAL, BOOL, BIGINT, BIT, TEXT ...

# 2, 3, 4, 5
os.chdir(r"C:\Users\Maryam\Desktop")

os.makedirs("Python")

open(r"Python\index.py", "x")

db = sqlite3.connect(r"Python\elzero.db")

cr = db.cursor()

cr.execute(
    "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT UNIQUE, birth_date DATE UNIQUE, email TEXT UNIQUE)")

fake = Faker()

for _ in range(5):
    cr.execute("INSERT OR IGNORE INTO users  (name, birth_date, email) VALUES (?, ?, ?)",
               (fake.name(), fake.date_of_birth(), fake.email()))
db.commit()

print("Last Row:", cr.execute("SELECT * FROM users ORDER BY id DESC LIMIT 1").fetchone())
print("#" * 10)

ID = int(input("Enter ID to Delete: "))

cr.execute("DELETE FROM users WHERE id = ?", (ID,))
db.commit()

if cr.rowcount > 0:
    print("User Deleted \nShow Other Data:")
    data = cr.execute("SELECT * FROM users ORDER BY id").fetchall()
    for row in data:
        print(f"ID => {row[0]}, Name => {row[1]}, Date Of Birth => {row[2]}, Email => {row[3]}")
else:
    print("User Not Found")

db.close()
