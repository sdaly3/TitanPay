from src.accounting.payment_method import PaymentMethod


class DirectDepositPayment(PaymentMethod):

    def __init__(self, emp, bank):
        PaymentMethod.__init__(emp)
        self.__bank = bank

    def pay(self, amt):
        print("Depositing $", amt, "in", self.__bank.get_bank_name(), "Account Number:", self.__bank.get_account_id,
          "using Routing Number:", self.__bank.get_routing_number)