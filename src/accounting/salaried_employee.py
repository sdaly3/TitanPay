class SalariedEmployee:
    def __init__(self, employee_id, first_name, last_name, salary, commission_rate, weekly_dues):
        self.__employee_id = ""
        self.__first_name = ""
        self.__last_name = ""
        self.__salary = ""
        self.__commission_rate = ""
        self.__weekly_dues = ""


    def get_full_name(self):
        return self.__last_name + ', ' + self.__first_name