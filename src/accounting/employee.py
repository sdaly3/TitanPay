class Employee:
    def __init__(self):
        self.__employee_id = ""
        self.__first_name = ""
        self.__last_name = ""
        self.__hourly_rate = ""
        self.__weekly_dues = ""

    def set_first_name(self, val):
        self.__first_name = val

    def set_last_name(self, val):
        self.__last_name = val

    def get_full_name(self):
        return self.__first_name + self.__last_name


