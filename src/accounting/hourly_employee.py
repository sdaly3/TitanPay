from src.accounting.employee import Employee
from src.accounting.time_card import TimeCard
from src.datetime import datetime


class HourlyEmployee(Employee, TimeCard):

    def __init__(self, employee_id, first_name, last_name, weekly_dues, hourly_rate, pay_method):
        Employee.__init__(self, employee_id, first_name, last_name, weekly_dues, pay_method)
        self.__hourly_rate = hourly_rate
        self.__time_cards = []

    def clock_in(self):
        tc = TimeCard(datetime.today())
        self.__time_cards.append(tc)

    def clock_out(self):
        for tc in self.__time_cards:
            if tc.get_date() == datetime.today():
                tc.clock_out()

    def pay(self, start_date, end_date):
        total_pay = 0
        for tc in self.__time_cards:
            if tc.get_date() > start_date and tc.get_date < end_date:
                total_pay += tc.calculate_daily_pay(self.__hourly_rate)
                self.get_payment_method(self).pay(total_pay)
