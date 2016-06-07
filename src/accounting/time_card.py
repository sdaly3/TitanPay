class TimeCard:

    def __init__(self, date, start_time, end_time):
        self.__date = date
        self.__start_time = start_time
        self.__end_time = end_time

    def calculate_daily_pay(self, rate, clock_in, clock_out, hours):
        rate = 15.00
        clock_in = self.__start_time.datetime.time(8, 00, 00)/3600
        clock_out = self.__end_time.datetime.time(5, 00, 00)/3600
        hours = clock_in - clock_out
        return sum(hours * 1.5)

# Professor Tillman - Am I on the right track?

#   if hours > 8:
#      overtime = hours - 8
#     return sum(overtime * (rate * 1.5))


