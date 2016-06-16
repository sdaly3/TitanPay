from src.accounting.employee import Employee
from src.accounting.receipt import Receipt


class SalariedEmployee(Employee, Receipt):

    def __init__(self, employee_id, first_name, last_name, weekly_dues, salary, commission_rate, pay_method):
        Employee.__init__(employee_id, first_name, last_name, weekly_dues, pay_method)
        self.__salary = salary
        self.__commission_rate = commission_rate
        self.__receipts = []

    def make_sale(self, double_amt):
        sale = Receipt("6/15/2016", 25.00)
        self.__receipts.append(sale)
