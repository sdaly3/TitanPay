from src.accounting.employee import Employee
from src.accounting.bank_account import BankAccount
from src.accounting.address import Address


def run():

    employee1 = Employee(1, "Stephanie", "Daly", 15.00)
    print(employee1.get_full_name())

    address = Address("123 Main Street", "Tampa", "FL", "33602")
    print(address.get_full_address())

    payday = BankAccount("Bank of America", 123456, 123456789)
    print(payday.deposit())


if __name__ == "__main__":
    run()