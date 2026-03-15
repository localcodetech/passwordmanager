import os
import tkinter as tk
from app.utils.apptheme import ThemeWidget

from tkinter import PhotoImage, filedialog, ttk
from PIL import Image, ImageFile, ImageTk

import pathlib
import time
from datetime import date
import json 
from json import JSONDecodeError


class HomeScreen(tk.Frame):
    def __init__(self, root, controller ):
        super().__init__(root, background="#35283a")
        self.controller = controller


        self.home_menu = tk.Menu(root,)
        root.configure(menu=self.home_menu)
        self.pack (expand=1, fill="both")
      

        self.home_menu_top = tk.Menu(self, tearoff=0)

        self.home_menu_top.add_command(label="exit", command=root.destroy)
        self.home_menu.add_cascade(menu=self.home_menu_top, label="file")


        self.subtOP_label = tk.Label(self,text=F"email: {""}, kwesi edutwem",foreground=ThemeWidget.foregroundcolor,background=ThemeWidget.loginPagebackgroundColor, width=10, height=2, anchor="n", ).pack(side="top", fill="x", )

        self.subtop_label2 = tk.Label(self,text="VAULTLANE PASSWORD MANAGER",font=("arial",15, "bold"),background=ThemeWidget.backgroundcolor, width=10, height=2, foreground=ThemeWidget.foregroundcolor, anchor="w").pack(side="top", fill="x")


        self.search_variable = tk.StringVar()
        self.search_entry = tk.Entry(self, textvariable=self.search_variable, bd=2,).place(x=1300, y=65)

       

        self.dateon_top = tk.Label(self, text=self.hometime_current(), bg=ThemeWidget.loginPagebackgroundColor,foreground=ThemeWidget.foregroundcolor).place(x=35, y=15)

        self.search_button = tk.Button(self, text="search", bd=2,
                  font=("arial", 10, "bold"), foreground=ThemeWidget.foregroundcolor, width=15,
                  background="#4285f4", compound="left").place(x=1515, y=62)
        



        
        self.home_label = tk.Button(self, text="Home", width=20, background=ThemeWidget.homepage_backgroundcolor, anchor="w",foreground=ThemeWidget.signuptextcolor, font=("arial",15, "bold"), relief="flat", highlightthickness=0).place(x=70, y=250)

        self.secureNote_label = tk.Button(self, text="Secure Note", width=20,anchor="w", background=ThemeWidget.homepage_backgroundcolor, foreground=ThemeWidget.signuptextcolor, font=("arial",15, "bold"), relief="flat", highlightthickness=0).place(x=70, y=300)        

        self.passwordview_label = tk.Button(self, text="Password", width=20, anchor="w",background=ThemeWidget.homepage_backgroundcolor, foreground=ThemeWidget.signuptextcolor, font=("arial",15, "bold"), relief="flat", highlightthickness=0).place(x=70, y=350)

        self.Personalinfo_label = tk.Button(self, text="Personal info", width=20, anchor="w",background=ThemeWidget.homepage_backgroundcolor, foreground=ThemeWidget.signuptextcolor, font=("arial",15, "bold"), relief="flat", highlightthickness=0).place(x=70, y=400)

        self.Ids_label = tk.Button(self, text="IDs", width=20,anchor="w",background=ThemeWidget.homepage_backgroundcolor, foreground=ThemeWidget.signuptextcolor, font=("arial",15, "bold"), relief="flat", highlightthickness=0).place(x=70, y=450)

        self.password_generator_label = tk.Button(self,text="Password Generator", width=20, background=ThemeWidget.homepage_backgroundcolor,anchor="w",foreground=ThemeWidget.signuptextcolor,font=("arial",15, "bold"), relief="flat", highlightthickness=0).place(x=70, y=500)

        self.passwrd_changer_label = tk.Button(self, text="Password Changer", width=20, anchor="w",background=ThemeWidget.homepage_backgroundcolor, foreground=ThemeWidget.signuptextcolor, font=("arial",15, "bold"), relief="flat", highlightthickness=0).place(x=70, y=550)



        
    

    def hometime_current(self):
       
       today = date.today()
       self.currentday = today.strftime("%d/%m/%y")
       return self.currentday

