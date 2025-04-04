#!/usr/bin/python3
import pathlib
import pygubu
PROJECT_PATH = pathlib.Path(__file__).parent
PROJECT_UI = PROJECT_PATH / "Tratment.ui"
from models import Treatment
from db import Session
from tkinter import messagebox
import random
import pygubuintertreatment_Main



class TratmentApp:
    def __init__(self, master=None):
        self.builder = builder = pygubu.Builder()
        builder.add_resource_path(PROJECT_PATH)
        builder.add_from_file(PROJECT_UI)
        # Main widget
        self.mainwindow = builder.get_object("toplevel1", master)
        builder.connect_callbacks(self)
        
       
        self.Codeuser = builder.get_object('entrycode')        
        self.Name = builder.get_object('entryname')     
        self.Description = builder.get_object('entrydescription')
        self.CodeTra = builder.get_object('entrycode')
        #tupla
        uivars = ('textVar_Code', 'textVar_Name', 'textVar_Description')          
        #le decimos constructor le decimos que trabaje con esas variables        
        builder.import_variables(self, uivars)   

    def run(self):
        self.mainwindow.mainloop()

    def randomCode(self):
        numberCode=random.randrange(100, 5000)
        code="t01-"+str(numberCode)
        self.textVar_Code.set(code)

    def funtion_include(self):
        session = Session()
        self.randomCode()
        
        treatment = Treatment(CodeTra = self.textVar_Code.get(),
                    Name = self.Name.get(),
                    Description = self.Description.get(),
                    Status = Treatment.States.ACTIVATED)

    
        session.add(treatment)
        session.commit()
        session.close()
        messagebox.showinfo( message='Treatment save!!', title='Information')

    def function_modify(self):
        session = Session()
        var_cod = self.CodeTra.get()
       
        treatment = session.query(Treatment).\
                  filter(Treatment.CodeTra==var_cod).\
                  update({'Name': self.Name.get(),
                          'Description': self.Description.get(), 
                        })

        session.commit()
        session.close()
        messagebox.showinfo( message='Treatment Modify!!', title='Modify')
        self.function_clean()

    def function_search(self):
        session = Session()
        var_cod = self.CodeTra.get()
        
        treatment = session.get(Treatment, str(var_cod))
        if(treatment!=None):
            self.textVar_Name.set(treatment.Name)
            self.textVar_Description.set(treatment.Description)
            messagebox.showinfo( message='Treatment found !!', title='Information')     
        else:
            messagebox.showerror( message='Treatment not found !!', title='Error')

    def function_clean(self):
        self.textVar_Code.set('')
        self.textVar_Name.set('')
        self.textVar_Description.set('')
       

    def function_delete(self):
        session = Session()
        var_cod = self.CodeTra.get()

        treatment = session.get(Treatment,self.CodeTra.get())
        
        if(str(treatment.Status)=='States.ACTIVATED'):
            treatment= session.query(Treatment).\
                    filter(Treatment.CodeTra==var_cod).\
                    update({'Status': 'INACTIVATED'})
            session.commit()
            session.close()
            messagebox.showinfo( message='Treatment Delete!!', title='Delete')
            self.function_clean()
        else:
            resp = messagebox.askquestion('Reactivated treatment','You want to reactivate the treatment?')
            treatment= session.query(Treatment).\
                        filter(Treatment.CodeTra==var_cod).\
                        update({'Status': 'ACTIVATED'})
            session.commit()
            session.close()
            messagebox.showinfo(message='Success reactivating treatment', title='Reactivated treatment')

    def function_showintermedial(self):
        tratment = pygubuintertreatment_Main.IntertreatmentApp()
        tratment.run()


if __name__ == "__main__":
    app = TratmentApp()
    app.run()
