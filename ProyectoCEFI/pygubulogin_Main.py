#!/usr/bin/python3
import pathlib
import pygubu
PROJECT_PATH = pathlib.Path(__file__).parent
PROJECT_UI = PROJECT_PATH / "login.ui"
import pygubu
import pygubumenu_Main
from tkinter import messagebox
from models import *
from db import Session 
import subprocess



class LoginApp:
    def __init__(self, master=None):
        self.builder = builder = pygubu.Builder()
        builder.add_resource_path(PROJECT_PATH)
        builder.add_from_file(PROJECT_UI)
        # Main widget
        self.mainwindow = builder.get_object("toplevellogin", master)

        self.User = builder.get_object('entryuser')        
        self.Password = builder.get_object('entrypassword')  


        #tupla
        uivars= ('textVar_Username', 'textVar_Password')
        #le decimos constructor le decimos que trabaje con esas variables        
        builder.import_variables(self, uivars)

        
        builder.connect_callbacks(self)

    def run(self):
        self.mainwindow.mainloop()

    def function_entry(self):
        sesion = Session()
        userX = sesion.get(User,self.textVar_Password.get())
        print(userX)
        #--------------------------------------------------
        type = userX.CodeRole
        role = sesion.get(Roles,type)
        print('The rol description is: ',role.Description)
        #--------------------------------------------------

        if((self.textVar_Username.get() == userX.Username) and (self.textVar_Password.get()== userX.Codeuser)):
            messagebox.showinfo(title='Found',message='Welcome!!')
            window = pygubumenu_Main.MenuApp (role.Description)
            window.run()

        else:
            messagebox.showerror(title='Error', message='The username or password is incorrect')    
        
        


    def function_clean(self):
        self.textVar_Username.set('')
        self.textVar_Password.set('')


if __name__ == "__main__":
    app = LoginApp()
    app.run()
