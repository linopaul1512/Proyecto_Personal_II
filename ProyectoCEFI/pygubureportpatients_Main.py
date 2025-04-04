#!/usr/bin/python3
import pathlib
import pygubu
PROJECT_PATH = pathlib.Path(__file__).parent
PROJECT_UI = PROJECT_PATH / "Reportpatients.ui"
from models import Patient
from tkinter import messagebox
from db import Session
import random
import tkinter as tk
from tkinter import ttk

class ReportpatientsApp:
    def __init__(self, master=None):
        self.builder = builder = pygubu.Builder()
        builder.add_resource_path(PROJECT_PATH)
        builder.add_from_file(PROJECT_UI)
        # Main widget
        self.mainwindow = builder.get_object("toplevel1", master)
        
        
    
        #tree view
        self.tree = builder.get_object('treeviewreport')
        columns = ('columnid', 'columnname', 'columnhours','columnphonenumber')

        
        #le decimos constructor le decimos que trabaje con esas variables
        builder.import_variables(self)
       
        #self.treeviewcon_diag.column("#1", delete=True)
        builder.connect_callbacks(self)

    def run(self):
        self.mainwindow.mainloop()

    def function_clean(self):
        pass

    def function_refresh(self):
        session = Session()
        patientx = session.query(Patient).all()
        
        
        if (patientx!=None):
            for x in patientx:
                self.tree.insert("",tk.END,values=(x.IDPat, x.Name, x.Birthdate, x.Phonenumber))
        else:
            messagebox.showinfo(message='Patient is null !!', title='Information')



if __name__ == "__main__":
    app = ReportpatientsApp()
    app.run()
