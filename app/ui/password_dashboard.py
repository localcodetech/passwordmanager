
import json
import os
import tkinter as tk
from tkinter import messagebox

from app.core.encryption import DataEncryption
from app.utils.apptheme import ThemeWidget
from firebase_admin import  db
from cryptography.fernet import Fernet





class PasswordDashboard(tk.Frame):

    
    def __init__(self, root, controller):
        super().__init__(root, background=ThemeWidget.homepage_backgroundcolor)
        self.controller = controller

        self.pack(expand=1, fill="both"
                  )
        self.filepath =os.path.join("app/database", "configuration.json")
        try:
            with open(file=self.filepath, mode="r", encoding="utf-8") as file:
                self.db_local = json.load(file)
        except (json.JSONDecodeError, FileNotFoundError):
            self.db_local = []

        

        self.subtOP_label = tk.Label(self,text=F"username: kwesi edutwem",foreground=ThemeWidget.foregroundcolor,background="#35283a", width=10, height=2, anchor="e", )
        self.subtOP_label.pack(side="top", fill="x", )

        self.subtop_label2 = tk.Label(self,text="VAULTLANE PASSWORD MANAGER",font=("arial",15, "bold"),background="#4d3f3c", width=10, height=2, foreground=ThemeWidget.foregroundcolor, anchor="center")
        self.subtop_label2.pack(side="top", fill="x")


        self.search_variable = tk.StringVar()
        self.search_entry = tk.Entry(self, textvariable=self.search_variable,).place(x=1300, y=65)


        self.search_button = tk.Button(self, text="search",
                  font=("arial", 10, "bold"), foreground=ThemeWidget.foregroundcolor, width=15,
                  background="#4285f4",command=self.searchonefile ,relief="flat").place(x=1515, y=62)

        from app.ui.home_page import HomeScreen
        self.go_to_homepage = tk.Button(self,command=lambda: self.controller.show_frames(HomeScreen) ,text="Home Screen",activebackground=ThemeWidget.foregroundcolor,width=20, anchor="w",background=ThemeWidget.homepage_backgroundcolor, foreground=ThemeWidget.signuptextcolor, font=("arial",15, "bold"), relief="flat", highlightthickness=0)
        self.go_to_homepage.place(x=30, y=900)
        

        self.subframe_for_add = tk.Frame(self,width=1500, height=1400,background="#ffffff" )
        self.subframe_for_add.pack(side="right")

        self.addinfo_labelframe = tk.LabelFrame(master=self.subframe_for_add, text="View Stored Data", borderwidth=1.0,background=ThemeWidget.addinfomationbox_bg_color,relief="groove" , labelanchor="nw")
        self.addinfo_labelframe.place(x=55,y=60, height=600, width=900)

        self.addlogin_label = tk.Label(master=self.addinfo_labelframe, text="Website", background=ThemeWidget.addinfomationbox_bg_color, justify="center", font=ThemeWidget.addinformation_text_font)
        self.addlogin_label.grid(row=0, column=0, padx=10)

        self.websitevar = tk.StringVar()
        self.addlogin_entry = tk.Entry(master=self.addinfo_labelframe,textvariable=self.websitevar,relief="flat" ,width=40)
        self.addlogin_entry.grid(row=0, column=1,padx=10, pady=20, ipady=5)

        self.addusername_label = tk.Label(master=self.addinfo_labelframe, text="username", background=ThemeWidget.addinfomationbox_bg_color, justify="center", font=ThemeWidget.addinformation_text_font)
        self.addusername_label.grid(row=1, column=0,  padx=10)

        self.usernamevar = tk.StringVar()
        self.addusername_entry = tk.Entry(master=self.addinfo_labelframe,textvariable=self.usernamevar,relief="flat" ,width=40)
        self.addusername_entry.grid(row=1, column=1,padx=10, pady=20, ipady=5)

        self.addpassword_label = tk.Label(master=self.addinfo_labelframe,relief="flat" ,text="password", background=ThemeWidget.addinfomationbox_bg_color, justify="center", font=ThemeWidget.addinformation_text_font)
        self.addpassword_label.grid(row=2, column=0 ,padx=10)


        self.passwordvar = tk.StringVar()
        self.addpassword_entry = tk.Entry(master=self.addinfo_labelframe,textvariable=self.passwordvar,relief="flat" ,width=40)
        self.addpassword_entry.grid(row=2, column=1, padx=10, pady=20, ipady=5)

        self.addemail_label = tk.Label(master=self.addinfo_labelframe, text="email", background=ThemeWidget.addinfomationbox_bg_color, justify="center", font=ThemeWidget.addinformation_text_font)
        self.addemail_label.grid(row=3, column=0,  padx=10)

        self.mailvar = tk.StringVar()
        self.addemail_entry = tk.Entry(master=self.addinfo_labelframe, textvariable=self.mailvar,relief="flat",width=40)
        self.addemail_entry.grid(row=3, column=1, padx=10, pady=20, ipady=5)

        self.addenote_label = tk.Label(master=self.addinfo_labelframe, text="note", background=ThemeWidget.addinfomationbox_bg_color, justify="center", font=ThemeWidget.addinformation_text_font)
        self.addenote_label.grid(row=4, column=0,  padx=10)


        
        self.addenote_entry = tk.Text(master=self.addinfo_labelframe ,relief="flat",width=40, height=5)
        self.addenote_entry.grid(row=4, column=1, padx=10,ipady=5 )
        
        self.upload_data = tk.Button(master=self.addinfo_labelframe, command=self.searchdata,text="View Data",relief="flat", width=25,background=ThemeWidget.addinfomationbox_bg_color, justify="center", font=ThemeWidget.addinformation_text_font)
        self.upload_data.grid(row=6, column=1,padx=10, pady=10, ipady=5)


    def searchdata(self):
        
            # ref = db.reference("users")

            
            # all_users = ref.get()
            
            # access_data = dict(all_users)
           
         if self.db_local:
            #     for userkey, uservalues in access_data.items():

            for uservalues in self.db_local:
                        website = uservalues.get("website")
                        username = uservalues.get("username")
                        email = uservalues.get("email")
                        scrambled_password = uservalues.get("password")
                        note = uservalues.get("note")
                      

                        # decrypdb = DataEncryption(database_config=scrambled_password)

                        # decodepassword = decrypdb.decryption()
                        # password = decodepassword.decode(encoding="utf-8")

                        self.websitevar.set(website)

                        self.mailvar.set(email)
                        self.passwordvar.set(scrambled_password)
                        self.usernamevar.set(username)
                        self.addenote_entry.insert("1.0", note)


         else:
                 messagebox.showinfo("","No data Found")


    def searchonefile(self):
         
       
        for uservalues in self.db_local:
        
        
            if uservalues:
                
                    if uservalues.get("username") == self.search_variable.get():
                            website = uservalues.get("website")
                            username = uservalues.get("username")
                            email = uservalues.get("email")
                            scrambled_password = uservalues.get("password")
                            note = uservalues.get("note")
                            

                          

                            self.websitevar.set(website)

                            self.mailvar.set(email)
                            self.passwordvar.set(scrambled_password)
                            self.usernamevar.set(username)
                            self.addenote_entry.insert("1.0", note)
                        
            



                     

                  
    





    


