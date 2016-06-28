from src.accounting.employee import Employee
from src.accounting.receipt import Receipt
from src.accounting import csv

class SalariedEmployee(Employee, Receipt):

    with open('salaried_employees.csv') as file:
        s_emp = csv.DictReader(file)
        for row in s_emp:
            print(row)

    def __init__(self, employee_id, first_name, last_name, weekly_dues, salary, commission_rate, pay_method):
        Employee.__init__(employee_id, first_name, last_name, weekly_dues, pay_method)
        self.__salary = salary
        self.__commission_rate = commission_rate
        self.__receipts = []

    def make_sale(self):
        sale = Receipt("6/15/2016", 25.00)
        self.__receipts.append(sale)

    def pay(self, start_date, end_date):
        total_pay = 0
        for sale in self.__receipts:
            if sale.get_date() > start_date and sale.get_date < end_date:
                total_pay += self.__salary + (self.__sale_amt * self.__commission_rate)

                self.get_payment_method(self).pay(total_pay)