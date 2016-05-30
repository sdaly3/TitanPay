class TimeCard:
    def __init__(self):
        self.__date = ""
        self.__start_time = ""
        self.__end_time = ""

    def calculate_daily_pay(rate):
        self.__hours = self.__start_time + self.__end_time
            if self.__hours > 8:
                self.__overtime = (rate * 1.5) * hours
            else
                self.__regular = rate * hours
          self.__total = self.__regular + self.__overtime