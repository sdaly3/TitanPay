import datetime

class TimeCard:
    def __init__(self, date, start_time, end_time):
        self.__date = ""
        self.__start_time = datetime.time(12, 55, 0)
        self.__end_time = datetime.time(13, 5, 0)
        hours = self.__start_time - self.__end_time
        print(hours)

   # def calculate_daily_pay(self, rate):
    #    if self.__start_time - self.__end_time
     #       overtime = (rate * 1.5) * hours
      #  else
       #     regular = rate * hours
        #    total = regular + overtime