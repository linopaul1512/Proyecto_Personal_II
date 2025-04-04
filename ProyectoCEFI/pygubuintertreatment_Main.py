#!/usr/bin/python3
import pathlib
import pygubu
PROJECT_PATH = pathlib.Path(__file__).parent
PROJECT_UI = PROJECT_PATH / "Intertreatment.ui"
from models import Consultation, Treatment, Treatment_Consultation
from tkinter import messagebox
from db import Session
import random
import tkinter as tk
from tkinter import ttk

class IntertreatmentApp:
    def __init__(self, master=None):
        self.builder = builder = pygubu.Builder()
        builder.add_resource_path(PROJECT_PATH)
        builder.add_from_file(PROJECT_UI)
        # Main widget
        self.mainwindow = builder.get_object("toplevel1", master)

       
        #Datos
        self.CodeCon = builder.get_object('entrycodecon')
        self.CodeTra = builder.get_object('entrycodetra')
        self.CodeTC = builder.get_object('entrycodetc')
        self.Effectiveness = builder.get_object('comboboxeffectiveness')

        #tree view
        self.tree = builder.get_object('treeviewcon_tre')
        columns = ('columncodetreatment', 'columnnamtreatment')

        #tupla
        uivars = ('textVar_CodeCon','textVar_CodeTra','textVar_CodTC', 'textVar_Effectiveness')  
        
        #le decimos constructor le decimos que trabaje con esas variables
        builder.import_variables(self, uivars)
       
        #self.treeviewcon_diag.column("#1", delete=True)
        builder.connect_callbacks(self)

       
    def run(self):
        self.mainwindow.mainloop()



    def funtion_include(self):
        session = Session()
        
        
        for row_cod in self.tree.get_children():
            row = self.tree.item(row_cod)['values']

            numberCode=random.randrange(100, 5000)
            code="i01-"+str(numberCode)
            
            
            if(self.textVar_Effectiveness.get() == "Success"):
                state = Treatment_Consultation.States.Success
            else: 
                state = Treatment_Consultation.States.Flop
           
            treatmentx = Treatment_Consultation(CodeTC = code,
                                    CodeTra = row[0],
                                    CodeCon = self.CodeCon.get(), 
                                    Effectiveness = state
                                    )
            session.add(treatmentx)
            session.commit()
            
        session.close()
        messagebox.showinfo( message='Treatment save!!', title='Information')

    def function_search(self):
        session = Session()
        var_cod = self.CodeTra.get()
        
        treatmentx = session.get(Treatment, str(var_cod))
        if (treatmentx!=None):
            messagebox.showinfo( message='Treatment found !!', title='Information') 

        else:
            messagebox.showerror(message='Treatment Not found !!', title='Error')


    def function_clean(self):
        self.textVar_CodeCon.set('')
        self.textVar_CodeTra.set('')
        self.textVar_Effectiveness.set('')

    def function_addintree(self):
        session = Session()
        var_cod = self.CodeTra.get()
        treatmentx = session.get(Treatment, str(var_cod))
     
        
        if (treatmentx!=None):
            self.tree.insert("",tk.END,values=(treatmentx.CodeTra, treatmentx.Name))

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
    app = IntertreatmentApp()
    app.run()
