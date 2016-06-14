class TimeCard:

    def __init__(self, date, start_time, end_time):
        self.__date = date
        self.__start_time = start_time
        self.__end_time = end_time

    def calculate_daily_pay(self, rate):
        hours = self.__start_time - self.__end_time
        if hours > 8:
            regular_pay = rate * 8
            overtime = (rate * 1.5) * (hours - 8)
            return regular_pay + overtime
        else:
            regular = rate * hours
            return regular




