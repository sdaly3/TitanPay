import sqlite3
from src.accounting import hourly_employee


def process_pay():
    conn = sqlite3.connect('payroll_db')
    c = conn.cursor()

    c.execute('SELECT * FROM hr_emp_tb INNER JOIN tc_tb ON hr_emp_tb.emp_id = tc_tb.emp_id')
    hr_rows = c.fetchall()
    for row in hr_rows:
        employee = hourly_employee.HourlyEmployee(row[0], row[2], row[1], row[3], row[4], row[5])
        print(employee)
        
        