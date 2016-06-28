from src.accounting import csv

class Receipt:

    with open('receipts.csv') as file:
        rec = csv.DictReader(file)
        for row in rec:
            print(row)

    def __init__(self, date, sale_amt):
        self.__date = date
        self.__sale_amt = sale_amt

    def get_date(self):
        return date