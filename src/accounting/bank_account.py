class BankAccount:

    def __init__(self, bank_name, routing_number, account_id):
        self.__bank_name = bank_name
        self.__routing_number = routing_number
        self.__account_id = account_id


    def deposit(self, amt=800):
        self.__amt = amt
        print("Depositing $", self.__amt, "in", self.__bank_name, "Account Number:", self.__account_id, "using Routing Number:", self.__routing_number)

