import sqlite3
from src.accounting import csv


def emp_import():
    conn = sqlite3.connect('payroll_db')
    c = conn.cursor()

    c.execute('DROP TABLE IF EXISTS hr_emp_tb')
    c.execute('DROP TABLE IF EXISTS s_emp_tb')
    c.execute('CREATE TABLE IF NOT EXISTS hr_emp_tb (emp_id INT PRIMARY KEY, last_name TEXT NOT NULL, first_name TEXT NOT NULL,\
     hr_rate REAL NOT NULL, union_dues INT NOT NULL, payment_method TEXT NOT NULL)')
    c.execute('CREATE TABLE IF NOT EXISTS s_emp_tb (emp_id INT PRIMARY KEY, last_name TEXT NOT NULL, first_name TEXT NOT NULL, \
     salary REAL NOT NULL, commission INT NOT NULL, union_dues INT NOT NULL, payment_method TEXT NOT NULL)')

    with open('hourly_employees.csv', 'r') as hr_emp:
        hr_read = csv.DictReader(hr_emp)
        enter = [(emp['EmployeeId'], emp['LastName'], emp['FirstName'], emp['HourlyRate'], emp['UnionDues'],
              emp['PaymentMethod']) for emp in hr_read]
    c.executemany('INSERT INTO hr_emp_tb (emp_id, last_name, first_name, hr_rate, union_dues, payment_method) VALUES \
                        (?, ?, ?, ?, ?, ?)', enter)

    with open('salaried_employees.csv', 'r') as s_emp:
        s_read = csv.DictReader(s_emp)
        enter = [(emp['EmployeeId'], emp['LastName'], emp['FirstName'], emp['Salary'], emp['CommissionRate'], emp['UnionDues'],
         emp['PaymentMethod']) for emp in s_read]
    c.executemany('INSERT INTO s_emp_tb (emp_id, last_name, first_name, salary, commission, union_dues, payment_method) VALUES \
                        (?, ?, ?, ?, ?, ?, ?)', enter)

    conn.commit()
    conn.close()