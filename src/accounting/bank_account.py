class BankAccount:

    def __init__(self, bank_name, routing_number, account_id):
        self.__bank_name = bank_name
        self.__routing_number = routing_number
        self.__account_id = account_id

    def get_bank_name(self):
        return self.__bank_name

    def get_routing_number(self):
        return self.__routing_number

    def get_account_id(self):
        return self.__account_id