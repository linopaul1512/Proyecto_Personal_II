#!/usr/bin/python3
import pathlib
import pygubu
PROJECT_PATH = pathlib.Path(__file__).parent
PROJECT_UI = PROJECT_PATH / "Client.ui"
from models import Client
from db import Session
from tkinter import messagebox
from datetime import datetime
from tkcalendar import DateEntry  


class ClientApp:
    def __init__(self, master=None):
        self.builder = builder = pygubu.Builder()
        builder.add_resource_path(PROJECT_PATH)
        builder.add_from_file(PROJECT_UI)
        # Main widget
        self.mainwindow = builder.get_object("toplevel1", master)

        self.IDCli = builder.get_object('entryid')        
        self.Name = builder.get_object('entryname')     
        self.Lastname = builder.get_object('entrylastname')
        self.Birthdate = builder.get_object('entrybirthdate')
        self.Adress = builder.get_object('entryadress')
        self.Phonenumber = builder.get_object('entryphonenumber')
        self.Email = builder.get_object('entryemail')
                             
        #tupla
        uivars = ('textVar_ID', 'textVar_Name', 'textVar_Lastname', 'textVar_Adress', 'textVar_Birthdate', 'textVar_Phonenumber', 'textVar_Email')                       

        #le decimos constructor le decimos que trabaje con esas variables        
        builder.import_variables(self, uivars)

        builder.connect_callbacks(self)

    def run(self):
        self.mainwindow.mainloop()

    def funtion_include(self):
        session = Session()

        # Obtiene la cadena de fecha del widget DateEntry
        birthdate_str = self.Birthdate.get()

        # Ajusta la cadena de fecha al formato esperado (d/m/yy -> dd/mm/yyyy)
        parts = birthdate_str.split('/')
        if len(parts) == 3:
            day, month, year = parts
            year = '20' + year if len(year) == 2 else year  # Convierte 'yy' en 'yyyy'
            birthdate_str = f'{day}/{month}/{year}'

        # Convierte la cadena de fecha en un objeto de fecha de Python
        birthdate = datetime.strptime(birthdate_str, "%d/%m/%Y").date()

        
        client = Client(ID=int(self.IDCli.get()),
                        Name=self.Name.get(),
                        Lastname=self.Lastname.get(),
                        Birthdate= birthdate,
                        Adress= self.Adress.get(),
                        Phonenumber=self.Phonenumber.get(),
                        Email=self.Email.get(),
                        Status=Client.States.ACTIVATED)
        
        session.add(client)
        session.commit()
        session.close()
        messagebox.showinfo(message='Client save!!', title='Information')

    def function_modify(self):
        session = Session()
        var_cod = self.IDCli.get()

        # Obtiene la cadena de fecha del widget DateEntry
        birthdate_str = self.Birthdate.get()

        # Ajusta la cadena de fecha al formato esperado (d/m/yy -> dd/mm/yyyy)
        parts = birthdate_str.split('/')
        if len(parts) == 3:
            day, month, year = parts
            year = '20' + year if len(year) == 2 else year  # Convierte 'yy' en 'yyyy'
            birthdate_str = f'{day}/{month}/{year}'

        # Convierte la cadena de fecha en un objeto de fecha de Python
        birthdate = datetime.strptime(birthdate_str, "%d/%m/%Y").date()
        
        client = session.query(Client).\
                  filter(Client.ID==var_cod).\
                  update({'Name': self.Name.get(),
                          'Lastname': self.Lastname.get(), 
                          'Birthdate': birthdate,
                          'Adress': self.Adress.get(),
                          'Phonenumber': self.Phonenumber.get(),
                          'Email': self.Email.get()
                        })

        session.commit()
        session.close()
        messagebox.showinfo( message='Client Modify!!', title='Modify')

    def function_delete(self):
        session = Session()
        var_cod = self.IDCli.get()

        clientx = session.get(Client,self.IDCli.get())
        
        if(str(clientx.Status)=='States.ACTIVATED'):
            clientx= session.query(Client).\
                    filter(Client.ID==var_cod).\
                    update({'Status': 'INACTIVATED'})
            session.commit()
            session.close()
            messagebox.showinfo( message='Client Delete!!', title='Delete')
            self.function_clean()
        else:
            resp = messagebox.askquestion('Reactivated client','You want to reactivate the client?')
            clientx= session.query(Client).\
                        filter(Client.ID==var_cod).\
                        update({'Status': 'ACTIVATED'})
            session.commit()
            session.close()
            messagebox.showinfo(message='Success reactivating client', title='Reactivated client')

    def function_search(self):
        session = Session()
        var_cod = self.IDCli.get()
 
        
        client = session.get(Client, str(var_cod))
        if(client!=None):
            self.textVar_Name.set(client.Name)
            self.textVar_Lastname.set(client.Lastname)
            self.textVar_Adress.set(client.Adress)
            self.textVar_Birthdate.set(client.Birthdate)
            self.textVar_Phonenumber.set(client.Phonenumber)
            self.textVar_Email.set(client.Email)
            messagebox.showinfo( message='Client found !!', title='Information')     
        else:
            messagebox.showerror( message='Client not found !!', title='Error')

    def function_clean(self):
        self.textVar_Name.set('')
        self.textVar_ID.set('')
        self.textVar_Lastname.set('')
        self.textVar_Adress.set('')
        self.textVar_Birthdate.set('')
        self.textVar_Phonenumber.set('')
        self.textVar_Email.set('')


if __name__ == "__main__":
    app = ClientApp()
    app.run()
