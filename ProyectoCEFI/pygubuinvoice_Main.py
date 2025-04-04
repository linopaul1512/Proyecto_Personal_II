#!/usr/bin/python3
import pathlib
import pygubu
PROJECT_PATH = pathlib.Path(__file__).parent
PROJECT_UI = PROJECT_PATH / "Invoice.ui"
from models import Client,Details_Invoice, Invoice, Consultation
from db import Session
from tkinter import messagebox
import random
import matplotlib 
import pandas

class InvoiceApp:
    def __init__(self, master=None):
        self.builder = builder = pygubu.Builder()
        builder.add_resource_path(PROJECT_PATH)
        builder.add_from_file(PROJECT_UI)
        # Main widget
        self.mainwindow = builder.get_object("toplevel1", master)

        self.CodeInvo = builder.get_object('entrycodeinvoice')        
        self.ID = builder.get_object('entryidclient')     
        self.Totalamount = builder.get_object('entrytotal')

        #tupla
        uivars = ('textVar_Codeinvoice', 'textVar_IDclient', 'textVar_Total')
        #le decimos constructor le decimos que trabaje con esas variables        
        builder.import_variables(self, uivars)

        builder.connect_callbacks(self)

    def run(self):
        self.mainwindow.mainloop()
    def randomCode(self):
        numberCode=random.randrange(100, 5000)
        code="i01-"+str(numberCode)
        self.textVar_Codeinvoice.set(code)

    def function_include(self):
        session = Session()
        self.randomCode()
       

        
        invoice = Invoice(CodeInvo=self.textVar_Codeinvoice.get(),
                        ID=self.ID.get(),
                        Totalamount= self.Totalamount.get(),
                        Status=Invoice.States.ACTIVATED)
        
        session.add(invoice)
        session.commit()
        session.close()
        messagebox.showinfo(message='Invoice save!!', title='Information')


if __name__ == "__main__":
    app = InvoiceApp()
    app.run()
