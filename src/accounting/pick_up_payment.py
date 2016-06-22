from src.accounting.payment_method import PaymentMethod


class PickUpPayment(PaymentMethod):

    def __init__(self, emp, address):
        PaymentMethod.__init__(emp)
        self.__address = address

    def pay(self, amt):
        print("A check for", amt, "is waiting for", self.__address.get_full_name(), "at the PostMaster")