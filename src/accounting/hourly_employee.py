from src.accounting.employee import Employee
from src.datetime import datetime, date

class HourlyEmployee(Employee):

    def __init__(self, employee_id, first_name, last_name, weekly_dues, hourly_rate, pay_method):
        Employee.__init__(self, employee_id, first_name, last_name, weekly_dues, pay_method)
        self.__hourly_rate = hourly_rate
        self.__time_cards = []

    def clock_in(self):
        today = date.today()
        start_time = datetime.now().time()
        self.__time_cards.append(today)
        self.__time_cards.append(start_time)

    def clock_out(self):
        end_time = datetime.now().time()
        self.__time_cards.append(end_time)

    def pay(self, start_date, end_date):


