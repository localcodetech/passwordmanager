import os
import tkinter as tk

from firebase_admin import db


from app.ui.secure_note import SecureNote
from app.utils.apptheme import ThemeWidget

from tkinter import  messagebox

from ..core.passwordgenerator import PasswordGenerator
from ..core.encryption import DataEncryption
from .password_dashboard import PasswordDashboard

from datetime import date
import json 
from json import JSONDecodeError


class HomeScreen(tk.Frame):

    


    def __init__(self, root, controller ):
        super().__init__(root, background=ThemeWidget.homepage_backgroundcolor)
        self.controller = controller


        self.filepath =os.path.join("app/database", "configuration.json")
        try:
            with open(file=self.filepath, mode="r", encoding="utf-8") as file:
                self.db_local = json.load(file)
        except (JSONDecodeError, FileNotFoundError):
            self.db_local = []


        self.home_menu = tk.Menu(root,)
        root.configure(menu=self.home_menu)
        self.pack (expand=1, fill="both")
      

        self.home_menu_top = tk.Menu(self, tearoff=0)

        self.home_menu_top.add_command(label="exit", command=root.destroy)
        self.home_menu.add_cascade(menu=self.home_menu_top, label="file")


        self.subtOP_label = tk.Label(self,text="User:  kwesi edutwem",foreground=ThemeWidget.foregroundcolor,background="#35283a", width=10, height=2, anchor="e", )
        self.subtOP_label.pack(side="top", fill="x", )

        self.subtop_label2 = tk.Label(self,text="VAULTLANE PASSWORD MANAGER",font=("arial",15, "bold"),background="#4d3f3c", width=10, height=2, foreground=ThemeWidget.foregroundcolor, anchor="w")
        self.subtop_label2.pack(side="top", fill="x")


        self.search_variable = tk.StringVar()
        self.search_entry = tk.Entry(self, textvariable=self.search_variable,).place(x=1300, y=65)

        
       
        Date = tk.StringVar()
        self.dateon_top = tk.Entry(self, textvariable=Date, relief="flat",justify="center",font=("Arial", 13, "bold"), width=10)
        self.dateon_top.place(x=70, y=10)
        Date.set(self.hometime_current())

        self.search_button = tk.Button(self, text="search",
                  font=("arial", 10, "bold"), foreground=ThemeWidget.foregroundcolor, width=15,
                  background="#4285f4", relief="flat").place(x=1515, y=62)
        
        
    

        
        self.home_label = tk.Button(self, text="Home",activebackground=ThemeWidget.foregroundcolor ,width=20, background=ThemeWidget.homepage_backgroundcolor, anchor="w",foreground=ThemeWidget.signuptextcolor, font=("arial",15, "bold"), relief="flat", highlightthickness=0)
        self.home_label.place(x=70, y=250)

        self.secureNote_label = tk.Button(self, text="Secure Note",activebackground=ThemeWidget.foregroundcolor, width=20,anchor="w", background=ThemeWidget.homepage_backgroundcolor, foreground=ThemeWidget.signuptextcolor, font=("arial",15, "bold"), relief="flat", highlightthickness=0, command=lambda: self.controller.show_frames(SecureNote))       
        self.secureNote_label.place(x=70, y=300) 


        self.passwordview_label = tk.Button(self,command=lambda:self.controller.show_frames(PasswordDashboard), text="Password", activebackground=ThemeWidget.foregroundcolor,width=20, anchor="w",background=ThemeWidget.homepage_backgroundcolor, foreground=ThemeWidget.signuptextcolor, font=("arial",15, "bold"), relief="flat", highlightthickness=0)
        self.passwordview_label.place(x=70, y=350)
       
        self.personalinfo_label = tk.Button(self, text="Personal info", activebackground=ThemeWidget.foregroundcolor,width=20, anchor="w",background=ThemeWidget.homepage_backgroundcolor, foreground=ThemeWidget.signuptextcolor, font=("arial",15, "bold"), relief="flat", highlightthickness=0)
        self.personalinfo_label.place(x=70, y=400)

        self.Ids_label = tk.Button(self, text="IDs", activebackground=ThemeWidget.foregroundcolor,width=20,anchor="w",background=ThemeWidget.homepage_backgroundcolor, foreground=ThemeWidget.signuptextcolor, font=("arial",15, "bold"), relief="flat", highlightthickness=0)
        self.Ids_label.place(x=70, y=450)


        self.password_generator_label = tk.Button(self,text="Password Generator",command=self.passwordgenerator_func ,activebackground=ThemeWidget.foregroundcolor,width=20, background=ThemeWidget.homepage_backgroundcolor,anchor="w",foreground=ThemeWidget.signuptextcolor,font=("arial",15, "bold"), relief="flat", highlightthickness=0)
        self.password_generator_label.place(x=70, y=500)


        self.logout_button = tk.Button(self,command=self.logout ,text="Log out",activebackground=ThemeWidget.foregroundcolor,width=20, anchor="w",background=ThemeWidget.homepage_backgroundcolor, foreground=ThemeWidget.signuptextcolor, font=("arial",15, "bold"), relief="flat", highlightthickness=0)
        self.logout_button.place(x=70, y=800)






        

        self.subframe_for_add = tk.Frame(self,width=1500, height=1400,background="#ffffff" )
        self.subframe_for_add.pack(side="right")

        self.addinfo_labelframe = tk.LabelFrame(master=self.subframe_for_add, text="Add New Logins", borderwidth=1.0,background=ThemeWidget.addinfomationbox_bg_color,relief="groove" , labelanchor="nw")
        self.addinfo_labelframe.place(x=55,y=60, height=600, width=900)

        self.addlogin_label = tk.Label(master=self.addinfo_labelframe, text="Website", background=ThemeWidget.addinfomationbox_bg_color, justify="center", font=ThemeWidget.addinformation_text_font)
        self.addlogin_label.grid(row=0, column=0, padx=10)

        self.addlogin_entry = tk.Entry(master=self.addinfo_labelframe,relief="flat" ,width=40)
        self.addlogin_entry.grid(row=0, column=1,padx=10, pady=20, ipady=5)

        self.addusername_label = tk.Label(master=self.addinfo_labelframe, text="username", background=ThemeWidget.addinfomationbox_bg_color, justify="center", font=ThemeWidget.addinformation_text_font)
        self.addusername_label.grid(row=1, column=0,  padx=10)

        self.addusername_entry = tk.Entry(master=self.addinfo_labelframe,relief="flat" ,width=40)
        self.addusername_entry.grid(row=1, column=1,padx=10, pady=20, ipady=5)

        self.addpassword_label = tk.Label(master=self.addinfo_labelframe,relief="flat" ,text="password", background=ThemeWidget.addinfomationbox_bg_color, justify="center", font=ThemeWidget.addinformation_text_font)
        self.addpassword_label.grid(row=2, column=0 ,padx=10)

        self.addpassword_entry = tk.Entry(master=self.addinfo_labelframe,relief="flat" ,width=40)
        self.addpassword_entry.grid(row=2, column=1, padx=10, pady=20, ipady=5)

        self.addemail_label = tk.Label(master=self.addinfo_labelframe, text="email", background=ThemeWidget.addinfomationbox_bg_color, justify="center", font=ThemeWidget.addinformation_text_font)
        self.addemail_label.grid(row=3, column=0,  padx=10)

        self.addemail_entry = tk.Entry(master=self.addinfo_labelframe, relief="flat",width=40)
        self.addemail_entry.grid(row=3, column=1, padx=10, pady=20, ipady=5)

        self.addenote_label = tk.Label(master=self.addinfo_labelframe, text="note", background=ThemeWidget.addinfomationbox_bg_color, justify="center", font=ThemeWidget.addinformation_text_font)
        self.addenote_label.grid(row=4, column=0,  padx=10)

        self.addenote_entry = tk.Text(master=self.addinfo_labelframe, relief="flat",width=40, height=5)
        self.addenote_entry.grid(row=4, column=1, padx=10,ipady=5 )
        
        self.upload_data = tk.Button(master=self.addinfo_labelframe, command=self.database_session,text="upload",relief="flat", width=25,background=ThemeWidget.addinfomationbox_bg_color, justify="center", font=ThemeWidget.addinformation_text_font)
        self.upload_data.grid(row=6, column=1,padx=10, pady=10, ipady=5)

        self.generator_pass = tk.IntVar(self)
        self.generatepassword_spinbox = tk.Spinbox(master=self, from_=8, to=32, width=26, textvariable=self.generator_pass)
        self.generatepassword_spinbox.place(x=70, y=550)

       

        self.password_textvar = tk.StringVar(self)
        self.entry_new_password = tk.Entry(master=self, relief="flat",textvariable=self.password_textvar, width=27)
        self.entry_new_password.place(y=600, x= 70)
        






    def passwordgenerator_func(self):
        value = self.generator_pass.get()
        self.newpassword = PasswordGenerator(length=value)
        f_password = self.newpassword.generation_of_password(length=value)

        self.password_textvar.set(f_password)
        

        
    
        



        
    

    def hometime_current(self):
       
       today = date.today()
       self.currentday = today.strftime("%d-%m-%y")
       return self.currentday


    def logout(self):
        answer = messagebox.askokcancel(title="", message="Do you want to Logout?")
        if answer == True:
            from app.ui.login_page import LoginScreen # import the loginscreen here
            self.controller.show_frames(LoginScreen)





    
    def database_session(self):
        self.website = self.addlogin_entry.get()
        self.email = self.addemail_entry.get()
        self.username = self.addusername_entry.get()
        self.password = self.addpassword_entry.get()
        self.note = self.addenote_entry.get("1.0", "end-1c")

    


        if self.website and self.email and self.username and self.password and self.note:
            data_serialize = json.dumps(self.password)
            data_for_encrption=data_serialize.encode("utf-8")
            print(f"before encryption: \n{data_for_encrption}")

            uploaddb = DataEncryption(database_config=data_for_encrption)
            encryted_data_db = uploaddb.encrytion_func()
            scrambled_password = encryted_data_db.decode("utf-8")
            print(scrambled_password)

            data_json = {
                "username" : self.username,
                "email" : self.email,
                "website" : self.website,
                "password" :  self.password ,
                "note" : self.note
            }
            self.db_local.append(data_json)


            with open(file=self.filepath, mode="w", encoding="utf-8") as file:
                json.dump(self.db_local, file, indent=4)

            ref = db.reference("users")

            new_user = ref.push(data_json)

            print(new_user)
            



        

            messagebox.showinfo("save", message="infomation saved")
        else:
            messagebox.showerror("error", message="all inputs not filled")




