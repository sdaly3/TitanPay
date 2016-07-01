from src.accounting import tkinter
from src.accounting import csv

class Menu:
    def __init__(self):
        self.___menu = tkinter.Tk()
        self.___menu.geometry("250x250")
        self.label1 = tkinter.Label(self.___menu)
        self.__process_btn = tkinter.Button(self.___menu, text='Process Payroll', command=self.process_payment)
        self.__process_btn.pack()

        tkinter.mainloop()

    def process_payment(self):
        with open('hourly_employees.csv') as file:
            hr_emp = csv.DictReader(file)
            for row in hr_emp:
                print(row)

pay = Menu()