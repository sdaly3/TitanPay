from src.accounting.employee import Employee
from src.accounting.address import Address


class MailPayment(Employee, Address):

    def __init__(self, amt):
        self.__amt = amt

    def pay(self):
        print("Mailing a check to", self.get_full_name(), "for", self.__amt, "to", self.get_full_address())