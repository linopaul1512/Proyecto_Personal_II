#!/usr/bin/python3
import pathlib
import pygubu
PROJECT_PATH = pathlib.Path(__file__).parent
PROJECT_UI = PROJECT_PATH / "Menu.ui"
import pygubuconsultation_Main, pygubudiagnosis_Main, pygubudetailsinvoice_Main,pygubuclient_Main, pygubuphysiotherapist, pygubutreatment_Main, pygubuuser_Main, pygubupatient_Main, pygubureportconsultation_Main, pygubutreatment_Main, pygubureportpatients_Main,pygubureportstatistical_Main, pygubuuser_Main
from models import *
from tkinter import DISABLED
import tkinter
from db import Session


class MenuApp:
    def __init__(self,type, master=None):
        self.builder = builder = pygubu.Builder()
        builder.add_resource_path(PROJECT_PATH)
        builder.add_from_file(PROJECT_UI)
        # Main widget
        self.mainwindow = builder.get_object("toplevel1", master)
        builder.connect_callbacks(self)
        self.type=type


        self.buttonuser = builder.get_object('buttonuser')
        self.buttonphysiotherapist = builder.get_object('buttonphysiotherapist')
        self.buttonconsultation = builder.get_object('buttonconsultation')
        self.buttonpatient = builder.get_object('buttonpatient')
        self.buttondiagnosis = builder.get_object('buttondiagnosis')
        self.buttonreportpatient = builder.get_object('buttonreportpatient')
        self.buttonreportconsultation = builder.get_object('buttonreportconsultation')
        self.butttonstatisticalreport = builder.get_object('buttonstatisticalreport')

        if (self.type!='Administrator'):
            self.buttonuser['state']='disabled'
           

    def run(self):
        self.mainwindow.mainloop()

    def function_user(self):
        user = pygubuuser_Main.UserApp()
        user.run()

    def function_patients(self):
        patients = pygubupatient_Main.PatientApp()
        patients.run()

    def function_physiotherapist(self):
        physiotherapist = pygubuphysiotherapist.PhysiotherapistApp()
        physiotherapist.run()

    def function_consultation(self):
        consultation = pygubuconsultation_Main.ConsultationApp()
        consultation.run()

    def function_diagnosis(self):
        diagnosis = pygubudiagnosis_Main.DiagnosisApp()
        diagnosis.run()

    def function_treatment(self):
        treatment = pygubutreatment_Main.TratmentApp()
        treatment.run()

    def function_reportpatients(self):
        report = pygubureportpatients_Main.ReportpatientsApp()
        report.run()

    def function_reportconsultation(self):
        report = pygubureportconsultation_Main.ReportconsultationApp()
        report.run()
    
    def function_reportstatistical(self):
        report = pygubureportstatistical_Main.StatisticalreportApp()
        report.run()

    def function_showinvoice(self):
        invoice = pygubudetailsinvoice_Main.DetailsinvoiceApp()
        invoice.run()
if __name__ == "__main__":
    app = MenuApp()
    app.run()
