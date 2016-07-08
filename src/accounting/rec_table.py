import sqlite3
from src.accounting import csv


def rec_import():
    conn = sqlite3.connect('payroll_db')
    c = conn.cursor()

    c.execute('DROP TABLE IF EXISTS rec_tb')
    c.execute('CREATE TABLE IF NOT EXISTS rec_tb (emp_id INT, last_name TEXT NOT NULL, item TEXT NOT NULL, \
    units INT NOT NULL, unit_cost REAL NOT NULL, total REAL NOT NULL)')


    with open('receipts.csv', 'r') as receipts:
        rec_read = csv.DictReader(receipts)
        enter = [(r['EmployeeId'], r['LastName'], r['Item'], r['Units'], r['UnitCost'], r['Total']) \
                 for r in rec_read]
    c.executemany('INSERT INTO rec_tb (emp_id, last_name, item, units, unit_cost, total) VALUES \
    (?, ?, ?, ?, ?, ?)', enter)

    conn.commit()
    conn.close()

