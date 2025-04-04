#!/usr/bin/python3
import pathlib
import pygubu
PROJECT_PATH = pathlib.Path(__file__).parent
PROJECT_UI = PROJECT_PATH / "Physiotherapist.ui"
from models import Physiotherapist
from db import Session
from tkinter import messagebox
from datetime import datetime
from tkcalendar import DateEntry  

class PhysiotherapistApp:
    def __init__(self, master=None):
        self.builder = builder = pygubu.Builder()
        builder.add_resource_path(PROJECT_PATH)
        builder.add_from_file(PROJECT_UI)
        # Main widget
        self.mainwindow = builder.get_object("toplevel1", master)
        
        self.IDPhy = builder.get_object('entryid')        
        self.Name = builder.get_object('entryname')     
        self.Lastname = builder.get_object('entrylastname')
        self.Birthdate = builder.get_object('entrybirthdate') 
        self.Adress = builder.get_object('entryadress')
        self.Salaryrate = builder.get_object('entrysalary')
        self.Phonenumber = builder.get_object('entryphonenumber')
        self.Email = builder.get_object('entryemail')
       
        #tupla
        uivars=('textVar_ID','textVar_Name','textVar_Lastname', 'textVar_Adress', 'textVar_Phonenumber', 'textVar_Email','textVar_Salary','textVar_Birthdate')
        
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
       
        
        physiotherapist = Physiotherapist(ID=int(self.IDPhy.get()),
                        Name=self.Name.get(),
                        Lastname=self.Lastname.get(),
                        Birthdate= birthdate,
                        Adress= self.Adress.get(),
                        Phonenumber=self.Phonenumber.get(),
                        Salaryrate=self.Salaryrate.get(),
                        Email=self.Email.get(),
                        Status=Physiotherapist.States.ACTIVATED)
        
        session.add(physiotherapist)
        session.commit()
        session.close()
        messagebox.showinfo(message='Physiotherapist save!!', title='Information')

    def function_modify(self):
        session = Session()
        var_cod = self.IDPhy.get()

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


        physiotherapist = session.query(Physiotherapist).\
                  filter(Physiotherapist.ID==var_cod).\
                  update({'Name': self.Name.get(),
                          'Lastname': self.Lastname.get(), 
                          'Birthdate': birthdate,
                          'Adress': self.Adress.get(),
                          'Salaryrate': self.Salaryrate.get(),
                          'Phonenumber': self.Phonenumber.get(),
                          'Email': self.Email.get()
                        })

        session.commit()
        session.close()
        messagebox.showinfo( message='Physiotherapist Modify!!', title='Modify')

    def function_delete(self):
        session = Session()
        var_cod = self.IDPhy.get()

        physiotherapist = session.get(Physiotherapist,self.IDPhy.get())
        
        if(str(physiotherapist.Status)=='States.ACTIVATED'):
            physiotherapist= session.query(Physiotherapist).\
                    filter(Physiotherapist.ID==var_cod).\
                    update({'Status': 'INACTIVATED'})
            session.commit()
            session.close()
            messagebox.showinfo( message='Physiotherapist Delete!!', title='Delete')
            self.function_clean()
        else:
            resp = messagebox.askquestion('Reactivated physiotherapist','You want to reactivate the physiotherapist?')
            physiotherapist= session.query(Physiotherapist).\
                        filter(Physiotherapist.ID==var_cod).\
                        update({'Status': 'ACTIVATED'})
            session.commit()
            session.close()
            messagebox.showinfo(message='Success reactivating physiotherapist', title='Reactivated physiotherapist')

    def function_search(self):
        session = Session()
        var_cod = self.IDPhy.get()
 
        
        physiotherapist = session.get(Physiotherapist, str(var_cod))
        if(physiotherapist!=None):
            self.textVar_Name.set(physiotherapist.Name)
            self.textVar_Lastname.set(physiotherapist.Lastname)
            self.textVar_Adress.set(physiotherapist.Adress)
            self.textVar_Birthdate.set(physiotherapist.Birthdate)
            self.textVar_Salary.set(physiotherapist.Salaryrate)
            self.textVar_Phonenumber.set(physiotherapist.Phonenumber)
            self.textVar_Email.set(physiotherapist.Email)
            messagebox.showinfo( message='Physiotherapist found !!', title='Information')     
        else:
            messagebox.showerror( message='Physiotherapist not found !!', title='Error')

    def function_clean(self):
        self.textVar_Name.set('')
        self.textVar_ID.set('')
        self.textVar_Lastname.set('')
        self.textVar_Birthdate.set('')
        self.textVar_Salary.set('')
        self.textVar_Phonenumber.set('')
        self.textVar_Email.set('')
        self.textVar_Adress.set('')


if __name__ == "__main__":
    app = PhysiotherapistApp()
    app.run()
