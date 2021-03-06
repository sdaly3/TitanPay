class Employee:

    def __init__(self, employee_id, first_name, last_name, weekly_dues, pay_method):
        self.__employee_id = employee_id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__weekly_dues = weekly_dues
        self.__pay_method = pay_method

    def get_full_name(self):
        return self.__last_name + ", " + self.__first_name

    def get_payment_method(self):
        return self.__pay_method