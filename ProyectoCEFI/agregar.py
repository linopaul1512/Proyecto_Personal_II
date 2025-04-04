from db import Session
from models import *

"""
def add_user():
    sesion = Session()
    userX = User(
        Codeuser='4444',
        Username = 'Lino',
        Passsword = '1234',
        Status = User.States.ACTIVATED,
        CodeRole = '777'        
    )
    sesion.add(userX)
    sesion.commit()
    sesion.close()
add_user()

"""



def add_role():
    session = Session()
    role = Roles(
        CodeRole='666',
        Description = 'Operator',
        Status = Roles.States.ACTIVATED
    )
    session.add(role)
    session.commit()
    session.close()
add_role()





"""
from datetime import datetime

# Listas de datos ficticios
nombres = ["Santiago", "Valentina", "Andrés", "Sofía", "Matías", "Camila", "Juan", "Valeria", "Diego", "Mariana", "Gabriel", "Carolina", "Sebastián", "Isabella", "Nicolás", "Gabriela", "Leonardo", "Daniela", "Carlos", "Laura", "Martín", "Antonella", "Rafael", "Renata", "Felipe", "Victoria", "Javier", "Alejandra", "David", "Natalia"]
apellidos = ["Rodríguez", "López", "González", "Pérez", "Martínez", "Sánchez", "García", "Fernández", "Ramírez", "Torres", "Morales", "Cruz", "González", "Ríos", "Díaz", "Castro", "Ruiz", "Herrera", "Ortega", "Núñez", "Jiménez", "Silva", "Mendoza", "Paredes", "Escobar", "Vargas", "Gómez", "Cordero", "Salazar", "Álvarez"]
telefonos = ["04121234567", "04261234567", "04141234567", "04121234568", "04121234569", "04261234568", "04261234569", "04141234568", "04141234569", "04121234566", "04261234566", "04141234566", "04141234565", "04261234565", "04261234564", "04141234564", "04121234564", "04121234563", "04141234563", "04261234563", "04261234562", "04121234562", "04261234561", "04141234561", "04141234562", "04121234561", "04261234560", "04141234560", "04141234559", "04121234559"]
correos = ["correo1@example.com", "correo2@example.com", "correo3@example.com", "correo4@example.com", "correo5@example.com", "correo6@example.com", "correo7@example.com", "correo8@example.com", "correo9@example.com", "correo10@example.com", "correo11@example.com", "correo12@example.com", "correo13@example.com", "correo14@example.com", "correo15@example.com", "correo16@example.com", "correo17@example.com", "correo18@example.com", "correo19@example.com", "correo20@example.com", "correo21@example.com", "correo22@example.com", "correo23@example.com", "correo24@example.com", "correo25@example.com", "correo26@example.com", "correo27@example.com", "correo28@example.com", "correo29@example.com", "correo30@example.com"]
fechas_nacimiento_str = ["30/12/1995", "15/04/1988", "20/08/1990", "05/03/2001", "10/11/1998", "25/06/1996", "14/02/1985", "12/07/2002", "03/09/1977", "18/01/1999", "09/05/1982", "07/12/2000", "21/06/1989", "19/04/1994", "08/11/1983", "16/10/2004", "11/02/1997", "28/03/2005", "23/09/1986", "02/01/1984", "24/07/1992", "22/06/1991", "01/05/1993", "04/08/1998", "06/12/1987", "17/10/1980", "13/03/1979", "19/09/1981", "27/04/2003", "26/08/1978"]
direcciones = ["Av. Bolívar, Caracas, Distrito Capital", "Calle 72, Maracaibo, Zulia", "Av. Andrés Eloy Blanco, Valencia, Carabobo", "Calle 25, Barquisimeto, Lara", "Calle 4, Mérida, Mérida", "Av. Las Delicias, Maracay, Aragua", "Calle 7, San Cristóbal, Táchira", "Av. Sucre, Cumaná, Sucre", "Av. Intercomunal, Puerto La Cruz, Anzoátegui", "Av. Alirio Ugarte Pelayo, Maturín, Monagas", "Av. Atlántico, Ciudad Guayana, Bolívar", "Av. Bolívar, Puerto Ordaz, Bolívar", "Calle 16, Barinas, Barinas", "Av. Carabobo, San Fernando de Apure, Apure", "Calle Zamora, Coro, Falcón", "Av. Santiago Mariño, Porlamar, Nueva Esparta", "Calle Los Baños, La Guaira, Vargas", "Av. Los Haticos, Punto Fijo, Falcón", "Av. Independencia, Los Teques, Miranda", "Calle Arismendi, Barcelona, Anzoátegui", "Calle El Progreso, San Juan de los Morros, Guárico", "Av. Bolívar, Trujillo, Trujillo", "Calle Gran Sabana, Santa Elena de Uairén, Bolívar", "Calle 3, El Tigre, Anzoátegui", "Av. Bolívar, Valera, Trujillo", "Av. Bolívar, Araure, Portuguesa", "Av. 5 de Julio, El Vigía, Mérida", "Av. Paseo Orinoco, Ciudad Bolívar, Bolívar", "Av. Intercomunal, Ciudad Ojeda, Zulia", "Av. La Industrial, Upata, Bolívar"]
cedulas = [12345678, 23456789, 34567890, 45678901, 56789012, 67890123, 78901234, 89012345, 90123456, 11234567, 22345678, 33456789, 44567890, 55678901, 66789012, 77890123, 88901234, 99012345, 4567777, 12301234, 23412345, 34512345, 45623456, 56723456, 67834567, 78934567, 89045678, 90145678, 11256789, 22356789.]
def add_patient1():
    session = Session()
    birthdate = datetime.strptime(fechas_nacimiento_str[0], "%d/%m/%Y").date()

    patient = Patient(
        IDPat=1234567,
        Name=nombres[0],
        Lastname=apellidos[0],
        Adress=direcciones[0],
        Birthdate=birthdate,
        Phonenumber=telefonos[0],
        Email=correos[0],
        Status=Patient.States.ACTIVATED
    )
    session.add(patient)
    session.commit()
    session.close()

    # Repite el patrón para add_patient2 a add_patient31
def add_patient2():
    session = Session()
    birthdate = datetime.strptime(fechas_nacimiento_str[1], "%d/%m/%Y").date()

    patient = Patient(
        IDPat=2345678,
        Name=nombres[1],
        Lastname=apellidos[1],
        Adress=direcciones[1],
        Birthdate=birthdate,
        Phonenumber=telefonos[1],
        Email=correos[1],
        Status=Patient.States.ACTIVATED
    )
    session.add(patient)
    session.commit()
    session.close()

def add_patient3():
    session = Session()
    birthdate = datetime.strptime(fechas_nacimiento_str[2], "%d/%m/%Y").date()

    patient = Patient(
        IDPat=1234563,
        Name=nombres[2],
        Lastname=apellidos[2],
        Adress=direcciones[2],
        Birthdate=birthdate,
        Phonenumber=telefonos[2],
        Email=correos[2],
        Status=Patient.States.ACTIVATED
    )
    session.add(patient)
    session.commit()
    session.close()

def add_patient4():
    session = Session()
    birthdate = datetime.strptime(fechas_nacimiento_str[3], "%d/%m/%Y").date()

    patient = Patient(
        IDPat=1234564,
        Name=nombres[3],
        Lastname=apellidos[3],
        Adress=direcciones[3],
        Birthdate=birthdate,
        Phonenumber=telefonos[3],
        Email=correos[3],
        Status=Patient.States.ACTIVATED
    )
    session.add(patient)
    session.commit()
    session.close()

def add_patient5():
    session = Session()
    birthdate = datetime.strptime(fechas_nacimiento_str[4], "%d/%m/%Y").date()

    patient = Patient(
        IDPat=1234565,
        Name=nombres[4],
        Lastname=apellidos[4],
        Adress=direcciones[4],
        Birthdate=birthdate,
        Phonenumber=telefonos[4],
        Email=correos[4],
        Status=Patient.States.ACTIVATED
    )
    session.add(patient)
    session.commit()
    session.close()

def add_patient6():
    session = Session()
    birthdate = datetime.strptime(fechas_nacimiento_str[5], "%d/%m/%Y").date()

    patient = Patient(
        IDPat=1234566,
        Name=nombres[5],
        Lastname=apellidos[5],
        Adress=direcciones[5],
        Birthdate=birthdate,
        Phonenumber=telefonos[5],
        Email=correos[5],
        Status=Patient.States.ACTIVATED
    )
    session.add(patient)
    session.commit()
    session.close()

def add_patient7():
    session = Session()
    birthdate = datetime.strptime(fechas_nacimiento_str[6], "%d/%m/%Y").date()

    patient = Patient(
        IDPat=1234573,
        Name=nombres[6],
        Lastname=apellidos[6],
        Adress=direcciones[6],
        Birthdate=birthdate,
        Phonenumber=telefonos[6],
        Email=correos[6],
        Status=Patient.States.ACTIVATED
    )
    session.add(patient)
    session.commit()
    session.close()

def add_patient8():
    session = Session()
    birthdate = datetime.strptime(fechas_nacimiento_str[7], "%d/%m/%Y").date()

    patient = Patient(
        IDPat=1234574,
        Name=nombres[7],
        Lastname=apellidos[7],
        Adress=direcciones[7],
        Birthdate=birthdate,
        Phonenumber=telefonos[7],
        Email=correos[7],
        Status=Patient.States.ACTIVATED
    )
    session.add(patient)
    session.commit()
    session.close()

    def add_patient9():
    session = Session()
    birthdate = datetime.strptime(fechas_nacimiento_str[8], "%d/%m/%Y").date()

    patient = Patient(
        IDPat=1234568,
        Name=nombres[8],
        Lastname=apellidos[8],
        Adress=direcciones[8],
        Birthdate=birthdate,
        Phonenumber=telefonos[8],
        Email=correos[8],
        Status=Patient.States.ACTIVATED
    )
    session.add(patient)
    session.commit()
    session.close()

def add_patient10():
    session = Session()
    birthdate = datetime.strptime(fechas_nacimiento_str[9], "%d/%m/%Y").date()

    patient = Patient(
        IDPat=1234569,
        Name=nombres[9],
        Lastname=apellidos[9],
        Adress=direcciones[9],
        Birthdate=birthdate,
        Phonenumber=telefonos[9],
        Email=correos[9],
        Status=Patient.States.ACTIVATED
    )
    session.add(patient)
    session.commit()
    session.close()

def add_patient11():
    session = Session()
    birthdate = datetime.strptime(fechas_nacimiento_str[10], "%d/%m/%Y").date()

    patient = Patient(
        IDPat=1234570,
        Name=nombres[10],
        Lastname=apellidos[10],
        Adress=direcciones[10],
        Birthdate=birthdate,
        Phonenumber=telefonos[10],
        Email=correos[10],
        Status=Patient.States.ACTIVATED
    )
    session.add(patient)
    session.commit()
    session.close()

def add_patient12():
    session = Session()
    birthdate = datetime.strptime(fechas_nacimiento_str[11], "%d/%m/%Y").date()

    patient = Patient(
        IDPat=1234571,
        Name=nombres[11],
        Lastname=apellidos[11],
        Adress=direcciones[11],
        Birthdate=birthdate,
        Phonenumber=telefonos[11],
        Email=correos[11],
        Status=Patient.States.ACTIVATED
    )
    session.add(patient)
    session.commit()
    session.close()

def add_patient13():
    session = Session()
    birthdate = datetime.strptime(fechas_nacimiento_str[12], "%d/%m/%Y").date()

    patient = Patient(
        IDPat=1234572,
        Name=nombres[12],
        Lastname=apellidos[12],
        Adress=direcciones[12],
        Birthdate=birthdate,
        Phonenumber=telefonos[12],
        Email=correos[12],
        Status=Patient.States.ACTIVATED
    )
    session.add(patient)
    session.commit()
    session.close()

def add_patient14():
    session = Session()
    birthdate = datetime.strptime(fechas_nacimiento_str[13], "%d/%m/%Y").date()

    patient = Patient(
        IDPat=1234573,
        Name=nombres[13],
        Lastname=apellidos[13],
        Adress=direcciones[13],
        Birthdate=birthdate,
        Phonenumber=telefonos[13],
        Email=correos[13],
        Status=Patient.States.ACTIVATED
    )
    session.add(patient)
    session.commit()
    session.close()

def add_patient15():
    session = Session()
    birthdate = datetime.strptime(fechas_nacimiento_str[14], "%d/%m/%Y").date()

    patient = Patient(
        IDPat=1234574,
        Name=nombres[14],
        Lastname=apellidos[14],
        Adress=direcciones[14],
        Birthdate=birthdate,
        Phonenumber=telefonos[14],
        Email=correos[14],
        Status=Patient.States.ACTIVATED
    )
    session.add(patient)
    session.commit()
    session.close()

def add_patient16():
    session = Session()
    birthdate = datetime.strptime(fechas_nacimiento_str[15], "%d/%m/%Y").date()

    patient = Patient(
        IDPat=1234575,
        Name=nombres[15],
        Lastname=apellidos[15],
        Adress=direcciones[15],
        Birthdate=birthdate,
        Phonenumber=telefonos[15],
        Email=correos[15],
        Status=Patient.States.ACTIVATED
    )
    session.add(patient)
    session.commit()
    session.close()

def add_patient17():
    session = Session()
    birthdate = datetime.strptime(fechas_nacimiento_str[16], "%d/%m/%Y").date()

    patient = Patient(
        IDPat=1234576,
        Name=nombres[16],
        Lastname=apellidos[16],
        Adress=direcciones[16],
        Birthdate=birthdate,
        Phonenumber=telefonos[16],
        Email=correos[16],
        Status=Patient.States.ACTIVATED
    )
    session.add(patient)
    session.commit()
    session.close()

def add_patient18():
    session = Session()
    birthdate = datetime.strptime(fechas_nacimiento_str[17], "%d/%m/%Y").date()

    patient = Patient(
        IDPat=1234577,
        Name=nombres[17],
        Lastname=apellidos[17],
        Adress=direcciones[17],
        Birthdate=birthdate,
        Phonenumber=telefonos[17],
        Email=correos[17],
        Status=Patient.States.ACTIVATED
    )
    session.add(patient)
    session.commit()
    session.close()

def add_patient19():
    session = Session()
    birthdate = datetime.strptime(fechas_nacimiento_str[18], "%d/%m/%Y").date()

    patient = Patient(
        IDPat=1234578,
        Name=nombres[18],
        Lastname=apellidos[18],
        Adress=direcciones[18],
        Birthdate=birthdate,
        Phonenumber=telefonos[18],
        Email=correos[18],
        Status=Patient.States.ACTIVATED
    )
    session.add(patient)
    session.commit()
    session.close()

def add_patient20():
    session = Session()
    birthdate = datetime.strptime(fechas_nacimiento_str[19], "%d/%m/%Y").date()

    patient = Patient(
        IDPat=1234579,
        Name=nombres[19],
        Lastname=apellidos[19],
        Adress=direcciones[19],
        Birthdate=birthdate,
        Phonenumber=telefonos[19],
        Email=correos[19],
        Status=Patient.States.ACTIVATED
    )
    session.add(patient)
    session.commit()
    session.close()
def add_patient21():
    session = Session()
    birthdate = datetime.strptime(fechas_nacimiento_str[20], "%d/%m/%Y").date()

    patient = Patient(
        IDPat=1234580,
        Name=nombres[20],
        Lastname=apellidos[20],
        Adress=direcciones[20],
        Birthdate=birthdate,
        Phonenumber=telefonos[20],
        Email=correos[20],
        Status=Patient.States.ACTIVATED
    )
    session.add(patient)
    session.commit()
    session.close()

def add_patient22():
    session = Session()
    birthdate = datetime.strptime(fechas_nacimiento_str[21], "%d/%m/%Y").date()

    patient = Patient(
        IDPat=1234581,
        Name=nombres[21],
        Lastname=apellidos[21],
        Adress=direcciones[21],
        Birthdate=birthdate,
        Phonenumber=telefonos[21],
        Email=correos[21],
        Status=Patient.States.ACTIVATED
    )
    session.add(patient)
    session.commit()
    session.close()

def add_patient23():
    session = Session()
    birthdate = datetime.strptime(fechas_nacimiento_str[22], "%d/%m/%Y").date()

    patient = Patient(
        IDPat=1234582,
        Name=nombres[22],
        Lastname=apellidos[22],
        Adress=direcciones[22],
        Birthdate=birthdate,
        Phonenumber=telefonos[22],
        Email=correos[22],
        Status=Patient.States.ACTIVATED
    )
    session.add(patient)
    session.commit()
    session.close()

def add_patient24():
    session = Session()
    birthdate = datetime.strptime(fechas_nacimiento_str[23], "%d/%m/%Y").date()

    patient = Patient(
        IDPat=1234583,
        Name=nombres[23],
        Lastname=apellidos[23],
        Adress=direcciones[23],
        Birthdate=birthdate,
        Phonenumber=telefonos[23],
        Email=correos[23],
        Status=Patient.States.ACTIVATED
    )
    session.add(patient)
    session.commit()
    session.close()

def add_patient25():
    session = Session()
    birthdate = datetime.strptime(fechas_nacimiento_str[24], "%d/%m/%Y").date()

    patient = Patient(
        IDPat=1234584,
        Name=nombres[24],
        Lastname=apellidos[24],
        Adress=direcciones[24],
        Birthdate=birthdate,
        Phonenumber=telefonos[24],
        Email=correos[24],
        Status=Patient.States.ACTIVATED
    )
    session.add(patient)
    session.commit()
    session.close()

def add_patient26():
    session = Session()
    birthdate = datetime.strptime(fechas_nacimiento_str[25], "%d/%m/%Y").date()

    patient = Patient(
        IDPat=1234585,
        Name=nombres[25],
        Lastname=apellidos[25],
        Adress=direcciones[25],
        Birthdate=birthdate,
        Phonenumber=telefonos[25],
        Email=correos[25],
        Status=Patient.States.ACTIVATED
    )
    session.add(patient)
    session.commit()
    session.close()

def add_patient27():
    session = Session()
    birthdate = datetime.strptime(fechas_nacimiento_str[26], "%d/%m/%Y").date()

    patient = Patient(
        IDPat=1234586,
        Name=nombres[26],
        Lastname=apellidos[26],
        Adress=direcciones[26],
        Birthdate=birthdate,
        Phonenumber=telefonos[26],
        Email=correos[26],
        Status=Patient.States.ACTIVATED
    )
    session.add(patient)
    session.commit()
    session.close()

def add_patient28():
    session = Session()
    birthdate = datetime.strptime(fechas_nacimiento_str[27], "%d/%m/%Y").date()

    patient = Patient(
        IDPat=1234587,
        Name=nombres[27],
        Lastname=apellidos[27],
        Adress=direcciones[27],
        Birthdate=birthdate,
        Phonenumber=telefonos[27],
        Email=correos[27],
        Status=Patient.States.ACTIVATED
    )
    session.add(patient)
    session.commit()
    session.close()

def add_patient29():
    session = Session()
    birthdate = datetime.strptime(fechas_nacimiento_str[28], "%d/%m/%Y").date()

    patient = Patient(
        IDPat=1234588,
        Name=nombres[28],
        Lastname=apellidos[28],
        Adress=direcciones[28],
        Birthdate=birthdate,
        Phonenumber=telefonos[28],
        Email=correos[28],
        Status=Patient.States.ACTIVATED
    )
    session.add(patient)
    session.commit()
    session.close()

def add_patient30():
    session = Session()
    birthdate = datetime.strptime(fechas_nacimiento_str[29], "%d/%m/%Y").date()

    patient = Patient(
        IDPat=1234589,
        Name=nombres[29],
        Lastname=apellidos[29],
        Adress=direcciones[29],
        Birthdate=birthdate,
        Phonenumber=telefonos[29],
        Email=correos[29],
        Status=Patient.States.ACTIVATED
    )
    session.add(patient)
    session.commit()
    session.close()


add_patient1()
add_patient2()
add_patient3()
add_patient4()
add_patient5()
add_patient6()
add_patient7()
add_patient8()
add_patient9()
add_patient10()
add_patient11()
add_patient12()
add_patient13()
add_patient14()
add_patient15()
add_patient16()
add_patient17()
add_patient18()
add_patient19()
add_patient20()
add_patient21()
add_patient22()
add_patient23()
add_patient24()
add_patient25()
add_patient26()
add_patient27()
add_patient28()
add_patient29()
add_patient30()

"""
