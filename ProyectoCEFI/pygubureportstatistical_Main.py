#!/usr/bin/python3
import pathlib
import pygubu
PROJECT_PATH = pathlib.Path(__file__).parent
PROJECT_UI = PROJECT_PATH / "StatisticalReport.ui"
from db import Session
from models import *
from collections import Counter
import matplotlib
import matplotlib.pyplot as plt
import pandas

class StatisticalreportApp:
    def __init__(self, master=None):
        self.builder = builder = pygubu.Builder()
        builder.add_resource_path(PROJECT_PATH)
        builder.add_from_file(PROJECT_UI)
        # Main widget
        self.mainwindow = builder.get_object("toplevel1", master)

        self.Casesgod  = builder.get_object('entrysuccessfultreatments')
        self.Fashiondiagnosis  = builder.get_object('entrydiagnosis')
        
        #tupla
        uivars = ('TextVar_Successfultreatments','textVar_Fashiondiagnois')
        builder.import_variables(self,uivars)

        builder.connect_callbacks(self)


    def run(self):
        self.mainwindow.mainloop()

    def function_clean(self):
        self.TextVar_Successfultreatments.set('')
        self.textVar_Fashiondiagnois.set('')

    def function_fashion(self):
        session = Session()
        # Obtener la lista de códigos de diagnóstico de la tabla Diagnosis_Consultation
        diagnosis_codes = [result[0] for result in session.query(Diagnosis_Consultation.CodeDI).all()]
        # Contar la frecuencia de cada código de diagnóstico
        counter = Counter(diagnosis_codes)
        # Encontrar el código de diagnóstico más común y su frecuencia
        most_common_code, _ = counter.most_common(1)[0]

        # Recuperar el nombre del diagnóstico a partir del código
        most_common_diagnosis = session.query(Diagnosis).filter_by(CodeDI=most_common_code).first()
        if most_common_diagnosis:
            self.textVar_Fashiondiagnois.set(most_common_diagnosis.Name)
        else:
            self.textVar_Fashiondiagnois.set("No se encontraron diagnósticos")
    
    def function_showgraph(self):
        session = Session()

        # Obtener la lista de códigos de diagnóstico de la tabla Diagnosis_Consultation
        diagnosis_codes = [result[0] for result in session.query(Diagnosis_Consultation.CodeDI).all()]

        # Contar la frecuencia de cada código de diagnóstico
        counter = Counter(diagnosis_codes)

        # Obtener los 5 diagnósticos más comunes
        N = 5  # Mostrar los 5 diagnósticos más comunes
        most_common = counter.most_common(N)

        # Separar los diagnósticos y sus frecuencias en listas separadas
        diagnoses, frequencies = zip(*most_common)

        # Obtener los nombres correspondientes a los códigos de diagnóstico
        diagnosis_names = []
        for code in diagnoses:
            diagnosis = session.query(Diagnosis).filter_by(CodeDI=code).first()
            if diagnosis:
                diagnosis_names.append(diagnosis.Name)
            else:
                diagnosis_names.append("Desconocido")

        # Crear una figura y un eje para la gráfica
        fig, ax = plt.subplots()

        # Crear un gráfico de barras con los diagnósticos en el eje X y las frecuencias en el eje Y
        ax.bar(diagnosis_names, frequencies)

        # Rotar las etiquetas del eje X para una mejor visualización si es necesario
        plt.xticks(rotation=45, ha="right")

        # Etiquetas de los ejes
        ax.set_xlabel('Diagnósticos')
        ax.set_ylabel('Frecuencia')


        # Título del gráfico
        ax.set_title('Diagnósticos más frecuentes')

        # Mostrar la gráfica
        plt.show()

        session.close()

    def function_percentage(self):
        session = Session()

        # Contar la cantidad de casos exitosos
        successful_cases = session.query(Treatment_Consultation).filter_by(Effectiveness='Success').count()

        # Contar el total de casos
        total_cases = session.query(Treatment_Consultation).count()

        if total_cases > 0:
            # Calcular el porcentaje de casos exitosos
            success_percentage = (successful_cases / total_cases) * 100

            # Mostrar el resultado en el Entry de porcentaje
            self.TextVar_Successfultreatments.set(success_percentage)
        else:
            self.TextVar_Successfultreatments.set(0)

        session.close()

     
        


if __name__ == "__main__":
    app = StatisticalreportApp()
    app.run()
