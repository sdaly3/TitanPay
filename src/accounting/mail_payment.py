from src.accounting.payment_method import PaymentMethod


class MailPayment(PaymentMethod):

    def __init__(self, emp, name, address):
        PaymentMethod.__init__(emp)
        self.__name = name
        self.__address = address

    def pay(self, amt):
        print("Mailing a check to", self.__name.get_full_name(), "for", amt, "to", self.__address.get_full_address())