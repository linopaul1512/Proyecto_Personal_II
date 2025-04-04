#!/usr/bin/python3
import pathlib
import pygubu
PROJECT_PATH = pathlib.Path(__file__).parent
PROJECT_UI = PROJECT_PATH / "Patient.ui"
from models import Patient
from db import Session
from tkinter import messagebox
from datetime import datetime




class PatientApp:
    def __init__(self, master=None):
        self.builder = builder = pygubu.Builder()
        builder.add_resource_path(PROJECT_PATH)
        builder.add_from_file(PROJECT_UI)
        # Main widget
        self.mainwindow = builder.get_object("toplevel1", master)
        builder.connect_callbacks(self)

        self.IDpatient = builder.get_object('entryid')        
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

        
        patient = Patient(IDPat=int(self.IDpatient.get()),
                        Name=self.Name.get(),
                        Lastname=self.Lastname.get(),
                        Birthdate= birthdate,
                        Adress= self.Adress.get(),
                        Phonenumber=self.Phonenumber.get(),
                        Email=self.Email.get(),
                        Status=Patient.States.ACTIVATED)
        
        session.add(patient)
        session.commit()
        session.close()
        messagebox.showinfo(message='Patient save!!', title='Information')
    
    def function_modify(self):
        session = Session()
        var_cod = self.IDpatient.get()

        
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
       
        patient= session.query(Patient).\
                  filter(Patient.IDPat==var_cod).\
                  update({'Name': self.Name.get(),
                          'Lastname': self.Lastname.get(), 
                          'Birthdate':  birthdate,
                          'Adress': self.Adress.get(),
                          'Phonenumber': self.Phonenumber.get(),
                          'Email': self.Email.get()
                        })

        session.commit()
        session.close()
        messagebox.showinfo( message='Patient Modify!!', title='Modify')
        self.function_clean()


    def function_delete(self):
        session = Session()
        var_cod = self.IDpatient.get()

        patientx = session.get(Patient,self.IDpatient.get())
        
        if(str(patientx.Status)=='States.ACTIVATED'):
            patientx= session.query(Patient).\
                    filter(Patient.IDPat==var_cod).\
                    update({'Status': 'INACTIVATED'})
            session.commit()
            session.close()
            messagebox.showinfo( message='Patient Delete!!', title='Delete')
            self.function_clean()
        else:
            resp = messagebox.askquestion('Reactivated patient','You want to reactivate the patient?')
            patientx= session.query(Patient).\
                        filter(Patient.IDPat==var_cod).\
                        update({'Status': 'ACTIVATED'})
            session.commit()
            session.close()
            messagebox.showinfo(message='Success reactivating patient', title='Reactivated patient')


    def function_search(self):
        session = Session()
        var_cod = self.IDpatient.get()
 
        
        patientx = session.get(Patient, str(var_cod))
        if(patientx!=None):
            self.textVar_Name.set(patientx.Name)
            self.textVar_Lastname.set(patientx.Lastname)
            self.textVar_Adress.set(patientx.Adress)
            self.textVar_Birthdate.set(patientx.Birthdate)
            self.textVar_Phonenumber.set(patientx.Phonenumber)
            self.textVar_Email.set(patientx.Email)
            messagebox.showinfo( message='Patient found !!', title='Information')     
        else:
            messagebox.showerror( message='Patient not found !!', title='Error')

    def function_clean(self):
        self.textVar_Name.set('')
        self.textVar_ID.set('')
        self.textVar_Lastname.set('')
        self.textVar_Adress.set('')
        self.textVar_Birthdate.set('')
        self.textVar_Phonenumber.set('')
        self.textVar_Email.set('')

if __name__ == "__main__":
    app = PatientApp()
    app.run()
