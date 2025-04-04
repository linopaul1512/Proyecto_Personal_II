#!/usr/bin/python3
import pathlib
import pygubu
PROJECT_PATH = pathlib.Path(__file__).parent
PROJECT_UI = PROJECT_PATH / "Interdiagnosis.ui"
from models import Consultation, Diagnosis, Diagnosis_Consultation
from tkinter import messagebox
from db import Session
import random

import tkinter as tk
from tkinter import ttk

class InterdiagnosisApp:
    def __init__(self, master=None):
        self.builder = builder = pygubu.Builder()
        builder.add_resource_path(PROJECT_PATH)
        builder.add_from_file(PROJECT_UI)
        # Main widget
        self.mainwindow = builder.get_object("toplevel1", master)   

        #Datos
        self.CodeCon = builder.get_object('entrycodecon')
        self.CodeDI = builder.get_object('entrycodedi')
        self.CodeDC = builder.get_object('entrycodedc')
        
        #tree view
        self.tree = builder.get_object('treeviewcon_diag')
        columns = ('columncodediagnosis', 'columnnamediagnosis')

        #tupla
        uivars = ('textVar_CodeCon', 'textVar_CodeDI', 'textVar_CodeDC')
        #le decimos constructor le decimos que trabaje con esas variables
        builder.import_variables(self, uivars)       

        builder.connect_callbacks(self)
   

    def run(self):
        self.mainwindow.mainloop()

  
    def funtion_include(self):
        session = Session()
       
        
        
        for row_cod in self.tree.get_children():
            row = self.tree.item(row_cod)['values']

            numberCode=random.randrange(100, 5000)
            code="i01-"+str(numberCode)

            diagnosisx = Diagnosis_Consultation(CodeDC = code,
                                    CodeDI = row[0],
                                    CodeCon = self.CodeCon.get()
                                    )
            session.add(diagnosisx)
            session.commit() 
        session.close()



        messagebox.showinfo( message='Diagnosis save!!', title='Information')

    def function_search(self):
        session = Session()
        var_cod = self.CodeDI.get()
        
        diagnosisx = session.get(Diagnosis, str(var_cod))
        if (diagnosisx!=None):
            messagebox.showinfo( message='Diagnosis found !!', title='Information') 

        else:
            messagebox.showerror(message='Diagnosis Not found !!', title='Error')

    def function_clean(self):
        self.textVar_CodeCon.set('')
        self.textVar_CodeDI.set('')
        """
        session = Session()
        var_cod = self.CodeDC.get()
        ordenx = session.get(Diagnosis, str(var_cod))
        session.delete(ordenx)
        session.commit()
        session.close()
        messagebox.showinfo( message='Orden delete!!', title='Delete')
        self.function_clean()"""

        

    def function_addintree(self):
        session = Session()
        var_cod = self.CodeDI.get()
        diagnosisx = session.get(Diagnosis, str(var_cod))
     
        
        if (diagnosisx!=None):
            self.tree.insert("",tk.END,values=(diagnosisx.CodeDI, diagnosisx.Name))

        else:
            messagebox.showinfo(message='No se pudo incluir !!', title='Information')      

    def function_searchconsultation(self):
        session = Session()
        var_cod = self.CodeCon.get()  

        consultationx = session.get(Consultation, str(var_cod))

        if(consultationx!=None):
            self.textVar_CodeCon.set(consultationx.CodeCon)
            messagebox.showinfo( message='Consultation found !!', title='Information') 
        else:
            messagebox.showerror( message='Consultation not found !!', title='Error') 


if __name__ == "__main__":
    app = InterdiagnosisApp()
    app.run()
