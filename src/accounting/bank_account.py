class BankAccount:
    def __init__(self):
        self.__bank_name = ""
        self.__routing_number = ""
        self.__account_id = ""

    def set_bank_name(self, val):
        self.__bank_name = val

    def set_routing_number(self, val):
        self.__routing_number = val

    def set_account_id(self, val):
        self.__account_id = val

    def get_bank_name(self):
        return self.__bank_name

    def get_routing_number(self):
        return self.__routing_number

    def get_account_id(self):
        return self.__account_id

if __name__ == "__main__":
        bank_name = BankAccount()
        routing_number = BankAccount()
        account_id = BankAccount()
        print(bank_name.get_bank_name(), routing_number.get_routing_number(), account_id.get_account_id())