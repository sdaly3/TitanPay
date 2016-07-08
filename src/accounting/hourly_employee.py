from src.accounting.employee import Employee
from src.accounting.time_card import TimeCard


class HourlyEmployee(Employee, TimeCard):

    def __init__(self, employee_id, first_name, last_name, weekly_dues, hourly_rate, pay_method):
        Employee.__init__(self, employee_id, first_name, last_name, weekly_dues, pay_method)
        self.__hourly_rate = hourly_rate
        self.__time_cards = []

    def clock_in(self):
        tc = TimeCard(date='1/1/16', start_time='800')
        self.__time_cards.append(tc)

    def clock_out(self):
        et = TimeCard(end_time='900')
        for tc in self.__time_cards:
            self.__time_cards.append(et)
            print(self.__time_cards)

    def pay(self, start_date, end_date):
        total_pay = 0
        for tc in self.__time_cards:
            if tc.get_date() > start_date and tc.get_date < end_date:
                total_pay += tc.calculate_daily_pay(self.__hourly_rate)
                self.get_payment_method(self).pay(total_pay)

