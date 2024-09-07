import sqlite3


conn = sqlite3.connect('employees.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS employees (
    employee_id INTEGER PRIMARY KEY,
    first_name VARCHAR(80),
    last_name VARCHAR(80),
    salary INTEGER,
    hire_date VARCHAR(80),
    city VARCHAR(80)
)
''')
conn.commit()

employees = [
    (1, 'Ali', 'Ahmadi', 600000, '2022-01-10', None),
    (2, 'Sara', 'Karami', 750000, '2021-05-15', 'Tehran'),
    (3, 'Reza', 'Mohammadi', 550000, '2023-02-20', 'Isfahan'),
    (4, 'Fatemeh', 'Rostami', 800000, '2022-08-30', None)
]

cursor.executemany('''
INSERT INTO employees (employee_id, first_name, last_name, salary, hire_date, city)
VALUES 
    (1, 'Ali', 'Ahmadi', 600000, '2022-01-10', None),
    (2, 'Sara', 'Karami', 750000, '2021-05-15', 'Tehran'),
    (3, 'Reza', 'Mohammadi', 550000, '2023-02-20', 'Isfahan'),
    (4, 'Fatemeh', 'Rostami', 800000, '2022-08-30', None)



''')

conn.commit()


cursor.execute('''
SELECT * FROM employees WHERE city IS NULL
''')
rows = cursor.fetchall()
print("رکوردهایی با city خالی:")
for row in rows:
    print(row)


cursor.execute('''
SELECT COUNT(*) FROM employees WHERE salary > 500000
''')
count = cursor.fetchone()
print(f"تعداد کارمندانی با حقوق بیشتر از 500000 تومان: {count}")

cursor.execute('''
SELECT employee_id, first_name, last_name, salary, 
       salary * .9 AS net_income
FROM employees
WHERE salary > 700000
ORDER BY net_income DESC
''')

rows = cursor.fetchall()
print("دریافتی کارمندانی با حقوق بیشتر از 700000 تومان:")
for row in rows:
    print(row)


cursor.execute('''
SELECT AVG(salary) FROM employees
''')
average_salary = cursor.fetchone()
print(f"میانگین حقوق کلیه کارمندان: {average_salary}")

cursor.execute('''
SELECT UPPER(first_name), UPPER(last_name), salary, hire_date, UPPER(city)
FROM employees
''')
rows = cursor.fetchall()
print("مشخصات کارمندان:")
for row in rows:
    print(row)


cursor.execute('''
UPDATE employees SET city = 'Mashhad'
''')
conn.commit()


cursor.execute('''
DELETE FROM employees WHERE city = 'Mashhad'
''')
conn.commit()

conn.close()