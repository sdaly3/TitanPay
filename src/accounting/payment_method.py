from src.accounting.employee import Employee
from src.accounting.mail_payment import MailPayment
from src.accounting.pick_up_payment import PickUpPayment
from src.accounting.direct_deposit import DirectDepositPayment


class PaymentMethod(Employee, MailPayment, PickUpPayment, DirectDepositPayment):

    def __init__(self):
        pass
