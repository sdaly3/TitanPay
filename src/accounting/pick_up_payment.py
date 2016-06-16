from src.accounting.employee import Employee


class PickUpPayment(Employee):

    def __init__(self, amt):
        self.__amt = amt

    def pay(self):
        print("A check for", self.__amt, "is waiting for", self.get_full_name(), "at the PostMaster")