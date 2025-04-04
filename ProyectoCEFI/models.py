from db import Base
from enum import Enum as Enumerador
from sqlalchemy import Column, Integer, String, Date, Enum, ForeignKey, Float, Boolean
from sqlalchemy.orm import relationship

class Physiotherapist(Base):

    class States(Enumerador):
       ACTIVATED = 'A'
       INACTIVATED = 'I'


    __tablename__ = 'physiotherapist'

    ID = Column(Integer, primary_key = True)
    Name = Column(String)
    Lastname = Column(String)   
    Adress = Column(String)
    Birthdate = Column(Date)
    Phonenumber = Column(String)
    Salaryrate = Column(Float)
    Email = Column(String)
    Status = Column(Enum(States))

    physiotherapistx = relationship('Consultation', back_populates='consultationx')
    
class Patient(Base):

    class States(Enumerador):
       ACTIVATED = 'A'
       INACTIVATED = 'I'


    __tablename__ = 'patient'

    IDPat = Column(Integer, primary_key = True)
    Name = Column(String)
    Lastname = Column(String)   
    Adress = Column(String)
    Birthdate = Column(Date)
    Phonenumber = Column(String)
    Email = Column(String)
    Status = Column(Enum(States))

    patientx = relationship('Consultation', back_populates='consultationx1')

class Client(Base):

    class States(Enumerador):
       ACTIVATED = 'A'
       INACTIVATED = 'I'


    __tablename__ = 'client'

    ID = Column(Integer, primary_key = True)
    Name = Column(String)
    Lastname = Column(String)   
    Adress = Column(String)
    Birthdate = Column(Date)
    Phonenumber = Column(String)
    Email = Column(String)
    Status = Column(Enum(States))

    clientx = relationship('Invoice', back_populates='consultationx4')

class Consultation(Base):

    class States(Enumerador):
       ACTIVATED = 'A'
       INACTIVATED = 'I'


    __tablename__ = 'consultation'

    CodeCon = Column(String, primary_key = True) 
    Date = Column(Date)
    Hours = Column(String)
    Price = Column(Float)
    Status = Column(Enum(States))

    #FK con paciente, fisioterapeuta 
    IDPat = Column(Integer, ForeignKey('patient.IDPat'))
    consultationx1 = relationship('Patient', back_populates='patientx')

    ID = Column(Integer, ForeignKey('physiotherapist.ID'))
    consultationx = relationship('Physiotherapist', back_populates='physiotherapistx')


    #relaciones 
    consultationx2 = relationship('Treatment_Consultation', back_populates='treatment_consultationx')
    consultationx3 = relationship('Diagnosis_Consultation', back_populates='diagnosis_consultationx')
    consultationx6 = relationship('Details_Invoice', back_populates='details_invoicex')

class Invoice(Base):

    class States(Enumerador):
       ACTIVATED = 'A'
       INACTIVATED = 'I'

    __tablename__ = 'invoice'

    CodeInvo = Column(String, primary_key = True)
    Totalamount = Column(Float)
    Status = Column(Enum(States))
    
    #FK
    ID = Column(Integer, ForeignKey('client.ID'))
    consultationx4 = relationship('Client', back_populates='clientx')

    #relacion
    invoicex = relationship('Details_Invoice', back_populates='detailsx')


class Details_Invoice(Base):

    class States(Enumerador):
       ACTIVATED = 'A'
       INACTIVATED = 'I'

    __tablename__ = 'details_invoice'
   
    CodeDET = Column(String, primary_key = True)
    

    #FK
    CodeInvo = Column(Integer, ForeignKey('invoice.CodeInvo'))
    detailsx = relationship('Invoice', back_populates='invoicex')
    #FK
    CodeCon = Column(Integer, ForeignKey('consultation.CodeCon'))
    details_invoicex = relationship('Consultation', back_populates='consultationx6')
    
    Quantity = Column(Integer)

class Diagnosis(Base):

    class States(Enumerador):
        ACTIVATED = 'A'
        INACTIVATED = 'I'
         
    __tablename__ = 'diagnosis'

    CodeDI = Column(String, primary_key = True)
    Name = Column(String)  
    Description = Column(String)
    Status = Column(Enum(States))

    tablediagnosisx = relationship('Diagnosis_Consultation', back_populates='diagnosisx')


class Diagnosis_Consultation(Base):


    __tablename__ = 'diagnosis_consultation'
    CodeDC = Column(String, primary_key= True)
   

    #FK
    CodeDI = Column(String, ForeignKey('diagnosis.CodeDI'))
    diagnosisx = relationship('Diagnosis', back_populates='tablediagnosisx')

    CodeCon = Column(String, ForeignKey('consultation.CodeCon'))
    diagnosis_consultationx = relationship('Consultation', back_populates='consultationx3')



class Treatment(Base):

    class States(Enumerador):
       ACTIVATED = 'A'
       INACTIVATED = 'I'


    __tablename__ = 'treatment'

    CodeTra = Column(String, primary_key = True)
    Name = Column(String)
    Description = Column(String)
    Status = Column(Enum(States))

    tabletreatmentx = relationship('Treatment_Consultation', back_populates='treatmentx')


class Treatment_Consultation(Base):

    class States(Enumerador):
       Success = 'S'
       Flop = 'F'

    __tablename__ = 'treatment_consultation'
    CodeTC = Column(String, primary_key= True)
    
    #FK
    CodeTra = Column(String, ForeignKey('treatment.CodeTra'))
    treatmentx = relationship('Treatment', back_populates='tabletreatmentx')

    CodeCon = Column(String, ForeignKey('consultation.CodeCon'))
    treatment_consultationx = relationship('Consultation', back_populates='consultationx2')

    Effectiveness =  Column(Enum(States))





class Roles(Base):

    class States(Enumerador):
       ACTIVATED = 'A'
       INACTIVATED = 'I'


    __tablename__ = 'roles'

    CodeRole = Column(Integer, primary_key = True)
    Description = Column(String)  
    Status = Column(Enum(States))

    user_rel = relationship('User', back_populates='rol_rel')

class User(Base):

    class States(Enumerador):
       ACTIVATED = 'A'
       INACTIVATED = 'I'


    __tablename__ = 'user'

    Codeuser = Column(String, primary_key = True)
    Name =  Column(String)
    Lastname = Column(String)
    Username = Column(String)
    Password = Column(String)   
    Status = Column(Enum(States))

    CodeRole = Column(Integer, ForeignKey('roles.CodeRole'))
    rol_rel = relationship('Roles', back_populates='user_rel')

