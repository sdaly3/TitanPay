import sqlite3
from src.accounting import csv


def tc_import():
    conn = sqlite3.connect('payroll_db')
    c = conn.cursor()

    c.execute('DROP TABLE IF EXISTS tc_tb')
    c.execute('CREATE TABLE IF NOT EXISTS tc_tb (emp_id INT, time_in INT NOT NULL, time_out INT NOT NULL, \
       date TEXT NOT NULL)')

    with open('timecards.csv', 'r') as t_card:
        tc_read = csv.DictReader(t_card)
        enter = [(tc['EmployeeId'], tc['In'], tc['Out'], tc['Date']) for tc in tc_read]
    c.executemany('INSERT INTO tc_tb (emp_id, time_in, time_out, date) VALUES (?, ?, ?, ?)', enter)

    conn.commit()
    conn.close()

