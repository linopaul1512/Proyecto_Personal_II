#!/usr/bin/python3
import pathlib
import pygubu
PROJECT_PATH = pathlib.Path(__file__).parent
PROJECT_UI = PROJECT_PATH / "Reportconsultation.ui"
from models import Consultation, Patient, Physiotherapist
from tkinter import messagebox
from db import Session
import random
import tkinter as tk
from tkinter import ttk

class ReportconsultationApp:
    def __init__(self, master=None):
        self.builder = builder = pygubu.Builder()
        builder.add_resource_path(PROJECT_PATH)
        builder.add_from_file(PROJECT_UI)
        # Main widget
        self.mainwindow = builder.get_object("toplevel1", master)
        builder.connect_callbacks(self)

       
    
        #tree view
        self.tree = builder.get_object('treeviewreport')
        columns = ('columncodecon', 'columndate', 'columnhours','columnpatient', 'columnphysiotherapist')

        #tupla
        #uivars = ('textVar_CodeCon','textVar_CodeTra')  
        
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
        consultationx = session.query(Consultation).all()

        
        if (consultationx!=None):
            # for c, i, f in session.query(Consultation, Patient, Physiotherapist).filter(Consultation.IDPat == Patient.IDPat).filter(Consultation.C == Physiotherapist.ID).all():
            for c, i in session.query(Consultation, Patient).filter(Consultation.IDPat == Patient.IDPat).all():
                self.tree.insert("",tk.END,values=(c.CodeCon, c.Date, c.Hours, i.Name))
        else:
            messagebox.showinfo(message='No se pudo incluir !!', title='Information')

             
        

if __name__ == "__main__":
    app = ReportconsultationApp()
    app.run()
