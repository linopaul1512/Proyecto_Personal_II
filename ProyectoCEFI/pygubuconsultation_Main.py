#!/usr/bin/python3
import pathlib
import pygubu
PROJECT_PATH = pathlib.Path(__file__).parent
PROJECT_UI = PROJECT_PATH / "Consultation.ui"
from models import Consultation, Patient, Physiotherapist
from db import Session
from tkinter import messagebox
from datetime import datetime
from tkcalendar import DateEntry 
import random

class ConsultationApp:
    def __init__(self, master=None):
        self.builder = builder = pygubu.Builder()
        builder.add_resource_path(PROJECT_PATH)
        builder.add_from_file(PROJECT_UI)
        # Main widget
        self.mainwindow = builder.get_object("toplevel2", master)

        self.CodeCons = builder.get_object('entrycodecon')        
        self.IDPat = builder.get_object('entrypatient')     
        self.IDPhy = builder.get_object('entryphysiotherapist')
        self.Date = builder.get_object('entrydate') 
        self.Price = builder.get_object('entryprice')
        self.Hours = builder.get_object('entryhours')
        
        
        #tupla
        uivars=('textVar_Codecon','textVar_Patient','textVar_Physiotherapist','textVar_Price','textVar_Hours', 'textVar_Date')
        #le decimos constructor le decimos que trabaje con esas variables        
        builder.import_variables(self, uivars)

        builder.connect_callbacks(self)

    def run(self):
        self.mainwindow.mainloop()

    def randomCode(self):
        numberCode=random.randrange(100, 5000)
        code="i01-"+str(numberCode)
        self.textVar_Codecon.set(code)

    def funtion_include(self):
        session = Session()
        self.randomCode()

        # Obtiene la cadena de fecha del widget DateEntry
        date_str = self.Date.get()

        # Ajusta la cadena de fecha al formato esperado (d/m/yy -> dd/mm/yyyy)
        parts = date_str.split('/')
        if len(parts) == 3:
            day, month, year = parts
            year = '20' + year if len(year) == 2 else year  # Convierte 'yy' en 'yyyy'
            date_str = f'{day}/{month}/{year}'

        # Convierte la cadena de fecha en un objeto de fecha de Python
        date = datetime.strptime(date_str, "%d/%m/%Y").date()
        
        consultation = Consultation (CodeCon = self.textVar_Codecon.get(),
                        Date= date,
                        Price= self.Price.get(),
                        IDPat= self.IDPat.get(),
                        ID=self.IDPhy.get(),
                        Hours=self.Hours.get(),
                        Status=Consultation.States.ACTIVATED)
        
        session.add(consultation)
        session.commit()
        session.close()
        messagebox.showinfo(message='Consultation save!!', title='Information')

    def function_modify(self):
        session = Session()
        var_cod = self.CodeCons.get()
       
       # Obtiene la cadena de fecha del widget DateEntry
        date_str = self.Date.get()

        # Ajusta la cadena de fecha al formato esperado (d/m/yy -> dd/mm/yyyy)
        parts = date_str.split('/')
        if len(parts) == 3:
            day, month, year = parts
            year = '20' + year if len(year) == 2 else year  # Convierte 'yy' en 'yyyy'
            date_str = f'{day}/{month}/{year}'

        # Convierte la cadena de fecha en un objeto de fecha de Python
        date = datetime.strptime(date_str, "%d/%m/%Y").date()
        
        consultation = session.query(Consultation).\
                  filter(Consultation.CodeCon==var_cod).\
                  update({'Date': date,
                          'Price': self.Price.get(), 
                          'IDPat': self.IDPat.get(),
                          'ID': self.IDPhy.get(),
                          'Hours': self.Hours.get()
                        })

        session.commit()
        session.close()
        messagebox.showinfo( message='Consultation Modify!!', title='Modify')

    def function_search(self):
        session = Session()
        var_cod = self.CodeCons.get()
 
        
        consultation = session.get(Consultation, str(var_cod))
        if(consultation!=None):
            self.textVar_Codecon.set(consultation.CodeCon)
            self.textVar_Patient.set(consultation.IDPat)
            self.textVar_Physiotherapist.set(consultation.ID)
            self.textVar_Price.set(consultation.Price)
            self.textVar_Hours.set(consultation.Hours)
            messagebox.showinfo( message='Consultation found !!', title='Information')     
        else:
            messagebox.showerror( message='Consultation not found !!', title='Error')

    def function_clean(self):
        self.textVar_Codecon.set('')
        self.textVar_Patient.set('')
        self.textVar_Physiotherapist.set('')
        self.textVar_Price.set('')
        self.textVar_Hours.set('')
        self.textVar_Date.set('')


    def function_delete(self):
        session = Session()
        var_cod = self.CodeCons.get()

        consultation = session.get(Consultation,self.CodeCons.get())
        
        if(str(consultation.Status)=='States.ACTIVATED'):
            consultation= session.query(Consultation).\
                    filter(Consultation.CodeCon==var_cod).\
                    update({'Status': 'INACTIVATED'})
            session.commit()
            session.close()
            messagebox.showinfo( message='Consultation Delete!!', title='Delete')
            self.function_clean()
        else:
            resp = messagebox.askquestion('Reactivated consultation','You want to reactivate the consultation?')
            consultation= session.query(Consultation).\
                        filter(Consultation.CodeCon==var_cod).\
                        update({'Status': 'ACTIVATED'})
            session.commit()
            session.close()
            messagebox.showinfo(message='Success reactivating consultation', title='Reactivated consultation')

    def function_searchpersons(self):
        session = Session()
        var_cod = self.IDPat.get()
        var_cod2 = self.IDPhy.get()
        
        patient = session.get(Patient, str(var_cod))
        physiotherapist = session.get(Physiotherapist, str(var_cod2))
        if(patient!=None and physiotherapist!=None ):
            messagebox.showinfo( message='Data found !!', title='Information')     
        else:
            messagebox.showerror( message='Some of the data was not found !!', title='Error')


if __name__ == "__main__":
    app = ConsultationApp()
    app.run()
