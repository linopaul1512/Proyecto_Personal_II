#!/usr/bin/python3
import pathlib
import pygubu
PROJECT_PATH = pathlib.Path(__file__).parent
PROJECT_UI = PROJECT_PATH / "Detailsinvoice.ui"
from models import  Invoice, Details_Invoice, Consultation, Client
from db import Session
from tkinter import messagebox
import random
import tkinter as tk
from tkinter import ttk
import matplotlib
import matplotlib.pyplot as plt

class DetailsinvoiceApp:
    def __init__(self, master=None):
        self.builder = builder = pygubu.Builder()
        builder.add_resource_path(PROJECT_PATH)
        builder.add_from_file(PROJECT_UI)
        # Main widget
        self.mainwindow = builder.get_object("toplevel1", master)
        
        self.total = 0

        #Datos
        self.CodeCon = builder.get_object('entrycodecon')
        self.IDClient = builder.get_object('entryidclient')
        self.CodeInvo = builder.get_object('entrycodeinvoice')
        self.Price = builder.get_object('entryprice')
        self.Total = builder.get_object('entrytotal')
        self.Name = builder.get_object('entrynameclient')
        #tree view
        self.tree = builder.get_object('treeviewcon_inv')
        columns = ('columncodecon', 'columnquantity')

        
        #tupla
        uivars = ('textVar_CodeCon','textVar_CodeInvoice', 'textVar_Quantity', 'textVar_Price', 'TextVar_Total', 'textVar_IDclient', 'textVar_Name')  
        
        #le decimos constructor le decimos que trabaje con esas variables
        builder.import_variables(self, uivars)
    
        #self.treeviewcon_diag.column("#1", delete=True)
        builder.connect_callbacks(self)

        

    def run(self):
        self.mainwindow.mainloop()


       
    
    def randomCode2(self):
        numberCode=random.randrange(100, 5000)
        code2="i01-"+str(numberCode)
        self.textVar_CodeInvoice.set(code2)


    def funtion_include(self):
        session = Session()
        #self.randomCode() 
        self.randomCode2()

        
        
       
        
        invoice = Invoice(CodeInvo = self.textVar_CodeInvoice.get(),
                        ID=self.IDClient.get(),
                        Totalamount= self.Total.get(),
                        Status=Invoice.States.ACTIVATED)
        
        session.add(invoice)
        session.commit()
       
        
        for row_cod in self.tree.get_children():
            
            numberCode=random.randrange(100, 5000)
            code="d01-"+str(numberCode)

            row = self.tree.item(row_cod)['values']

            detailsinvoice = Details_Invoice(CodeDET = code,
                                    CodeInvo = self.CodeInvo.get(),
                                    CodeCon = row[0],
                                    Quantity =  row[1]
                                    )
            session.add(detailsinvoice)
            session.commit()
        session.close()

        messagebox.showinfo( message='Invoice save!!', title='Information')

    def function_search(self):
        session = Session()
        var_cod = self.CodeInvo.get()
        
        invoice = session.get(Invoice, str(var_cod))
        if (invoice!=None):
            messagebox.showinfo( message='Invoice found !!', title='Information') 

        else:
            messagebox.showerror(message='Invoice Not found !!', title='Error')

    def function_clean(self):
        self.textVar_CodeCon.set('')
        self.textVar_CodeInvoice.set('')
        self.textVar_Quantity.set('')
        self.textVar_Price.set('')
        self.TextVar_Total.set('')
        self.textVar_IDclient.set('')
        self.textVar_Name.set('')

    def function_addintree(self):
        quantity = self.textVar_Quantity.get()
        price = self.textVar_Price.get()
        
        if (self.textVar_CodeCon.get()!=None and self.textVar_Quantity.get()!=None):
            self.tree.insert("",tk.END,values=(self.textVar_CodeCon.get(), self.textVar_Quantity.get() ))
            

            quantity = int(quantity)
            self.total = self.total + (quantity * price)
            self.TextVar_Total.set(self.total)
        
        else:
            messagebox.showerror( message='Filling in the information fields is mandatory !!', title='Error')
   
    def function_searchconsultation(self):
        session = Session()
        var_cod = self.CodeCon.get()  

        consultationx = session.get(Consultation, str(var_cod))

        if(consultationx!=None):
            self.textVar_CodeCon.set(consultationx.CodeCon)
            self.textVar_Price.set(consultationx.Price)
            messagebox.showinfo( message='Consultation found !!', title='Information') 
        else:
            messagebox.showerror( message='Consultation not found !!', title='Error')
    

    def function_searchclient(self):
        session = Session()
        var_cod = self.IDClient.get()  

        client = session.get(Client, str(var_cod))

        if(client!=None):
            self.textVar_Name.set(client.Name)
            messagebox.showinfo( message='Client found !!', title='Information') 
        else:
            messagebox.showerror( message='Client not found !!', title='Error')


   
if __name__ == "__main__":
    app = DetailsinvoiceApp()
    app.run()
