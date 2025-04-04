#!/usr/bin/python3
import pathlib
import pygubu
PROJECT_PATH = pathlib.Path(__file__).parent
PROJECT_UI = PROJECT_PATH / "User.ui"
from models import User
from models import Roles
from db import Session
from tkinter import messagebox
import random

class UserApp:
    def __init__(self, master=None):
        self.builder = builder = pygubu.Builder()
        builder.add_resource_path(PROJECT_PATH)
        builder.add_from_file(PROJECT_UI)
        # Main widget
        self.mainwindow = builder.get_object("toplevel1", master)
        builder.connect_callbacks(self)
        self.Codeuser = builder.get_object('entrycode')        
        self.Name = builder.get_object('entryname')     
        self.Lastname = builder.get_object('entrylastname')
        self.Username = builder.get_object('entryusername')        
        self.Password = builder.get_object('entrypassword')
        self.Role = builder.get_object('comboboxrole')

        #tupla
        uivars = ('textVar_Name','textVar_Code','textVar_Lastname', 'textVar_Username', 'textVar_Password', 'textVar_Role')          
        #le decimos constructor le decimos que trabaje con esas variables        
        builder.import_variables(self, uivars)       


    def run(self):
        self.mainwindow.mainloop()

    def randomCode(self):
        numberCode=random.randrange(100, 5000)
        code="u01-"+str(numberCode)
        self.textVar_Code.set(code)
        


    def funtion_include(self):
        session = Session()
        self.randomCode()
        
        if(self.textVar_Role.get() == "Operator"):
            codrole = "666"
        else: codrole = "777"
        
        user = User(Codeuser =  self.textVar_Code.get(),
                    Name = self.Name.get(),
                    Username = self.Username.get(),
                    Lastname = self.Lastname.get(),
                    Password = self.Password.get(),
                    CodeRole = codrole,
                    Status = User.States.ACTIVATED)
       
    
        session.add(user)
        session.commit()
        session.close()
        messagebox.showinfo( message='User save!!', title='Information')       

    def function_modify(self):
        session = Session()
        var_cod = self.Codeuser.get()
       
        userx= session.query(User).\
                  filter(User.Codeuser==var_cod).\
                  update({'Name': self.Name.get(),
                          'Username': self.Username.get(),
                          'Lastname': self.Lastname.get(), 
                        })

        session.commit()
        session.close()
        messagebox.showinfo( message='User Modify!!', title='Modify')
        self.function_clean()


    def function_search(self):
        session = Session()
        var_cod = self.Codeuser.get()

       
 
        
        userx = session.get(User, str(var_cod))
        if(userx!=None):
            self.textVar_Name.set(userx.Name)
            self.textVar_Lastname.set(userx.Lastname)
            self.textVar_Username.set(userx.Username)
            if userx.CodeRole == "666":
                self.Role.set("Operator")
            else:
                self.Role.set("Administrator")
                 
            messagebox.showinfo( message='User found !!', title='Information')     
        else:
            messagebox.showerror( message='User not found !!', title='Error')

    def function_clean(self):
        self.textVar_Name.set('')
        self.textVar_Code.set('')
        self.textVar_Lastname.set('')
        self.textVar_Username.set('')
        self.textVar_Password.set('')
        self.textVar_Role.set('')       
     

    def function_delete(self):
        session = Session()
        var_cod = self.Codeuser.get()

        userx = session.get(User,self.Codeuser.get())
        
        if(str(userx.Status)=='States.ACTIVATED'):
            userx= session.query(User).\
                    filter(User.Codeuser==var_cod).\
                    update({'Status': 'INACTIVATED'})
            session.commit()
            session.close()
            messagebox.showinfo( message='User Delete!!', title='Delete')
            self.function_clean()
        else:
            resp = messagebox.askquestion('Reactivated User','You want to reactivate the user?')
            userx= session.query(User).\
                        filter(User.Codeuser==var_cod).\
                        update({'Status': 'ACTIVATED'})
            session.commit()
            session.close()
            messagebox.showinfo(message='Success reactivating user', title='Reactivated user')


if __name__ == "__main__":
    app = UserApp()
    app.run()
