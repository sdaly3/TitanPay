from src.datetime import datetime, date


class TimeCard:

    def __init__(self, date):
        self.__date = date

    def clock_in(self):
        self.__start_time = datetime.now().time()

    def clock_out(self):
        self.__end_time = datetime.now().time()

    def get_date(self):
        return date

    def calculate_daily_pay(self, rate):
        hours = self.__start_time - self.__end_time
        if hours > 8:
            regular_pay = rate * 8
            overtime = (rate * 1.5) * (hours - 8)
            return regular_pay + overtime
        else:
            regular = rate * hours
            return regular




