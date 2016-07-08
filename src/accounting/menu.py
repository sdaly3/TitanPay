from src.accounting import tkinter
from src.accounting.emp_table import emp_import
from src.accounting.tc_table import tc_import
from src.accounting.rec_table import rec_import
from src.accounting.pay_employees import process_pay


class Menu:
    def __init__(self):
        self.___menu = tkinter.Tk()
        self.___menu.geometry("250x250")
        self.__label1 = tkinter.Label(self.___menu, text='Payroll Data')
        self.__emp_btn = tkinter.Button(self.___menu, text='Import Employees', command=emp_import)
        self.__emp_btn.pack()
        self.__tc_btn = tkinter.Button(self.___menu, text='Import Timecards', command=tc_import)
        self.__tc_btn.pack()
        self.__emp_btn = tkinter.Button(self.___menu, text='Import Receipts', command=rec_import)
        self.__emp_btn.pack()
        self.__process_btn = tkinter.Button(self.___menu, text='Process Payroll', command=process_pay)
        self.__process_btn.pack()
        self.__label1.pack()

        tkinter.mainloop()


pay = Menu()