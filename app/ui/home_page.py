import os
import tkinter as tk


from app.utils.apptheme import ThemeWidget

from tkinter import PhotoImage, filedialog, ttk, messagebox

from ..core.passwordgenerator import PasswordGenerator

import pathlib
import time
from datetime import date
import json 
from json import JSONDecodeError


class HomeScreen(tk.Frame):
    def __init__(self, root, controller ):
        super().__init__(root, background=ThemeWidget.homepage_backgroundcolor)
        self.controller = controller


        self.home_menu = tk.Menu(root,)
        root.configure(menu=self.home_menu)
        self.pack (expand=1, fill="both")
      

        self.home_menu_top = tk.Menu(self, tearoff=0)

        self.home_menu_top.add_command(label="exit", command=root.destroy)
        self.home_menu.add_cascade(menu=self.home_menu_top, label="file")


        self.subtOP_label = tk.Label(self,text=F"email: {""}, kwesi edutwem",foreground=ThemeWidget.foregroundcolor,background="#35283a", width=10, height=2, anchor="e", )
        self.subtOP_label.pack(side="top", fill="x", )

        self.subtop_label2 = tk.Label(self,text="VAULTLANE PASSWORD MANAGER",font=("arial",15, "bold"),background="#4d3f3c", width=10, height=2, foreground=ThemeWidget.foregroundcolor, anchor="w")
        self.subtop_label2.pack(side="top", fill="x")


        self.search_variable = tk.StringVar()
        self.search_entry = tk.Entry(self, textvariable=self.search_variable, bd=2,).place(x=1300, y=65)

        
       
        Date = tk.StringVar()
        self.dateon_top = tk.Entry(self, textvariable=Date, justify="center",font=("Arial", 13, "bold"), width=10)
        self.dateon_top.place(x=70, y=10)
        Date.set(self.hometime_current())

        self.search_button = tk.Button(self, text="search", bd=2,
                  font=("arial", 10, "bold"), foreground=ThemeWidget.foregroundcolor, width=15,
                  background="#4285f4", compound="left").place(x=1515, y=62)
        
        
    

        
        self.home_label = tk.Button(self, text="Home",activebackground=ThemeWidget.foregroundcolor ,width=20, background=ThemeWidget.homepage_backgroundcolor, anchor="w",foreground=ThemeWidget.signuptextcolor, font=("arial",15, "bold"), relief="flat", highlightthickness=0)
        self.home_label.place(x=70, y=250)

        self.secureNote_label = tk.Button(self, text="Secure Note",activebackground=ThemeWidget.foregroundcolor, width=20,anchor="w", background=ThemeWidget.homepage_backgroundcolor, foreground=ThemeWidget.signuptextcolor, font=("arial",15, "bold"), relief="flat", highlightthickness=0)       
        self.secureNote_label.place(x=70, y=300) 

        self.passwordview_label = tk.Button(self, text="Password", activebackground=ThemeWidget.foregroundcolor,width=20, anchor="w",background=ThemeWidget.homepage_backgroundcolor, foreground=ThemeWidget.signuptextcolor, font=("arial",15, "bold"), relief="flat", highlightthickness=0)
        self.passwordview_label.place(x=70, y=350)
       
        self.personalinfo_label = tk.Button(self, text="Personal info", activebackground=ThemeWidget.foregroundcolor,width=20, anchor="w",background=ThemeWidget.homepage_backgroundcolor, foreground=ThemeWidget.signuptextcolor, font=("arial",15, "bold"), relief="flat", highlightthickness=0)
        self.personalinfo_label.place(x=70, y=400)

        self.Ids_label = tk.Button(self, text="IDs", activebackground=ThemeWidget.foregroundcolor,width=20,anchor="w",background=ThemeWidget.homepage_backgroundcolor, foreground=ThemeWidget.signuptextcolor, font=("arial",15, "bold"), relief="flat", highlightthickness=0)
        self.Ids_label.place(x=70, y=450)


        self.password_generator_label = tk.Button(self,text="Password Generator",command=self.passwordgenerator_func ,activebackground=ThemeWidget.foregroundcolor,width=20, background=ThemeWidget.homepage_backgroundcolor,anchor="w",foreground=ThemeWidget.signuptextcolor,font=("arial",15, "bold"), relief="flat", highlightthickness=0)
        self.password_generator_label.place(x=70, y=500)

        self.passwrd_changer_label = tk.Button(self, text="Password Changer", activebackground=ThemeWidget.foregroundcolor,width=20, anchor="w",background=ThemeWidget.homepage_backgroundcolor, foreground=ThemeWidget.signuptextcolor, font=("arial",15, "bold"), relief="flat", highlightthickness=0)
        self.passwrd_changer_label.place(x=70, y=650)

        self.logout_button = tk.Button(self,command=self.logout ,text="Log out",activebackground=ThemeWidget.foregroundcolor,width=20, anchor="w",background=ThemeWidget.homepage_backgroundcolor, foreground=ThemeWidget.signuptextcolor, font=("arial",15, "bold"), relief="flat", highlightthickness=0)
        self.logout_button.place(x=70, y=800)


        

        self.subframe_for_add = tk.Frame(self,width=1500, height=1400,background="#ffffff" )
        self.subframe_for_add.pack(side="right")

        self.addinfo_labelframe = tk.LabelFrame(master=self.subframe_for_add, text="Add New Logins", borderwidth=1.0,background=ThemeWidget.addinfomationbox_bg_color,relief="groove" , labelanchor="n")
        self.addinfo_labelframe.place(x=55,y=60, height=500, width=1200)

        self.addlogin_label = tk.Label(master=self.addinfo_labelframe, text="Website", background=ThemeWidget.addinfomationbox_bg_color, justify="center", font=ThemeWidget.addinformation_text_font)
        self.addlogin_label.grid(row=0, column=0, padx=10)

        self.addlogin_entry = tk.Entry(master=self.addinfo_labelframe, width=40)
        self.addlogin_entry.grid(row=0, column=1,padx=10, pady=20)

        self.addusername_label = tk.Label(master=self.addinfo_labelframe, text="username", background=ThemeWidget.addinfomationbox_bg_color, justify="center", font=ThemeWidget.addinformation_text_font)
        self.addusername_label.grid(row=1, column=0,  padx=10)

        self.addusername_entry = tk.Entry(master=self.addinfo_labelframe, width=40)
        self.addusername_entry.grid(row=1, column=1,padx=10, pady=20)

        self.addpassword_label = tk.Label(master=self.addinfo_labelframe, text="password", background=ThemeWidget.addinfomationbox_bg_color, justify="center", font=ThemeWidget.addinformation_text_font)
        self.addpassword_label.grid(row=2, column=0 ,padx=10)

        self.addpassword_entry = tk.Entry(master=self.addinfo_labelframe, width=40)
        self.addpassword_entry.grid(row=2, column=1, padx=10, pady=20)

        self.addemail_label = tk.Label(master=self.addinfo_labelframe, text="email", background=ThemeWidget.addinfomationbox_bg_color, justify="center", font=ThemeWidget.addinformation_text_font)
        self.addemail_label.grid(row=3, column=0,  padx=10)

        self.addemail_entry = tk.Entry(master=self.addinfo_labelframe, width=40)
        self.addemail_entry.grid(row=3, column=1, padx=10, pady=20)

        self.addenote_label = tk.Label(master=self.addinfo_labelframe, text="note", background=ThemeWidget.addinfomationbox_bg_color, justify="center", font=ThemeWidget.addinformation_text_font)
        self.addenote_label.grid(row=4, column=0,  padx=10)

        self.addenote_entry = tk.Text(master=self.addinfo_labelframe, width=40, height=5)
        self.addenote_entry.grid(row=4, column=1, padx=10, )
        
        self.addpassword_length = tk.Label(master=self.addinfo_labelframe, text="Password Length", background=ThemeWidget.addinfomationbox_bg_color, justify="center", font=ThemeWidget.addinformation_text_font)
        self.addpassword_length.grid(row=6, column=0, padx=10)

        self.generator_pass = tk.IntVar(self)
        self.generatepassword_spinbox = tk.Spinbox(master=self, from_=8, to=32, width=10, textvariable=self.generator_pass)
        self.generatepassword_spinbox.place(x=70, y=550)

        

        self.password_textvar = tk.StringVar(self)
        self.entry_new_password = tk.Entry(master=self, textvariable=self.password_textvar, width=40)
        self.entry_new_password.place(y=600, x= 70)
        






    def passwordgenerator_func(self):
        value = self.generator_pass.get()
        self.newpassword = PasswordGenerator(length=value)
        f_password = self.newpassword.generation_of_password(length=value)

        self.password_textvar.set(f_password)
        

        
    
        



        
        


# add



        
    

    def hometime_current(self):
       
       today = date.today()
       self.currentday = today.strftime("%d-%m-%y")
       return self.currentday


    def logout(self):
        answer = messagebox.askokcancel(title="", message="Do you want to Logout?")
        if answer == True:
            from app.ui.login_page import LoginScreen # import the loginscreen here
            self.controller.show_frames(LoginScreen)
