from src.accounting.bank_account import BankAccount


class DirectDepositPayment(BankAccount):

    def __init__(self, amt):
        self.__amt = amt

    def pay(self):
        print("Depositing $", self.__amt, "in", self.__bank_name, "Account Number:", self.__account_id,
          "using Routing Number:", self.__routing_number)