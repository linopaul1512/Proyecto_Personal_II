#!/usr/bin/python3
import pathlib
import pygubu
PROJECT_PATH = pathlib.Path(__file__).parent
PROJECT_UI = PROJECT_PATH / "Diagnosis.ui"
from models import Diagnosis
from db import Session
from tkinter import messagebox
import random
import pyguinterdiagnosis_main

class DiagnosisApp:
    def __init__(self, master=None):
        self.builder = builder = pygubu.Builder()
        builder.add_resource_path(PROJECT_PATH)
        builder.add_from_file(PROJECT_UI)
        # Main widget
        self.mainwindow = builder.get_object("toplevel1", master)
        builder.connect_callbacks(self)


        self.CodeDI = builder.get_object('entrycode')        
        self.Name = builder.get_object('entryname')    
        self.Description = builder.get_object('entrydescription')

        #tupla
        uivars = ('textVar_Code','textVar_Name', 'textVar_Description')          
        #le decimos constructor le decimos que trabaje con esas variables        
        builder.import_variables(self, uivars) 
        
    
    def run(self):
        self.mainwindow.mainloop()

    def randomCode(self):
        numberCode=random.randrange(100, 5000)
        code="d01-"+str(numberCode)
        self.textVar_Code.set(code)
    
    def funtion_include(self):
        session = Session()
        self.randomCode()
        
        
        diagnosis = Diagnosis(CodeDI =  self.textVar_Code.get(),
                              Name = self.Name.get(),
                              Description = self.Description.get(),
                              Status = Diagnosis.States.ACTIVATED)
            
    
        session.add(diagnosis)
        session.commit()
        session.close()
        messagebox.showinfo( message='Diagnosis save!!', title='Information')  

    def function_modify(self):
        session = Session()
        var_cod = self.CodeDI.get()
       
        diagnosis= session.query(Diagnosis).\
                  filter(Diagnosis.CodeDI==var_cod).\
                  update({'Name': self.Name.get(),
                          'Description': self.Description.get(),
                        })

        session.commit()
        session.close()
        messagebox.showinfo( message='Diagnosis Modify!!', title='Modify')
        self.function_clean()


    def function_search(self):
        session = Session()
        var_cod = self.CodeDI.get()

        
        diagnosis = session.get(Diagnosis, str(var_cod))
        if(diagnosis!=None):
            self.textVar_Name.set(diagnosis.Name)
            self.textVar_Description.set(diagnosis.Description)
            
            messagebox.showinfo( message='Diagnosis found !!', title='Information')     
        else:
            messagebox.showerror( message='Diagnosis not found !!', title='Error')

    def function_clean(self):
        self.textVar_Name.set('')
        self.textVar_Code.set('')
        self.textVar_Description.set('')

    def function_delete(self):
        session = Session()
        var_cod = self.CodeDI.get()

        diagnosis = session.get(Diagnosis,self.CodeDI.get())
        
        if(str(diagnosis.Status)=='States.ACTIVATED'):
            diagnosis= session.query(Diagnosis).\
                    filter(Diagnosis.CodeDI==var_cod).\
                    update({'Status': 'INACTIVATED'})
            session.commit()
            session.close()
            messagebox.showinfo( message='Diagnosis Delete!!', title='Delete')
            self.function_clean()
        else:
            resp = messagebox.askquestion('Reactivated Diagnosis','You want to reactivate the diagnosis?')
            diagnosis= session.query(Diagnosis).\
                        filter(Diagnosis.CodeDI==var_cod).\
                        update({'Status': 'ACTIVATED'})
            session.commit()
            session.close()
            messagebox.showinfo(message='Success reactivating diagnosis', title='Reactivated diagnosis')

    def function_showintermedial(self):
        diagnosis = pyguinterdiagnosis_main.InterdiagnosisApp()
        diagnosis.run()


if __name__ == "__main__":
    app = DiagnosisApp()
    app.run()
