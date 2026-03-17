
import json
import socket

import keyring
import email_validator

import tkinter as tk
from tkinter import messagebox, ttk

from requests import HTTPError
import requests

from app.ui.home_page import HomeScreen
from app.utils.apptheme import ThemeWidget

from firebase_webapi import FirebaseRestApi

class LoginScreen(tk.Frame):
    def __init__(self,  root, controller ):  
        super().__init__(root,background=ThemeWidget.homepage_backgroundcolor)
        
        self.controller = controller
        self.pack(expand=1, anchor="center", fill="both")


        tk.Frame.columnconfigure(self, 0, weight=1)
        tk.Frame.columnconfigure(self,1, weight=1)
        tk.Frame.rowconfigure(self, 0, weight=1)
        
      
        self.welcometext = ttk.Label(self, text="Welcome Back",font=ThemeWidget.welcome_font, background=ThemeWidget.homepage_backgroundcolor, foreground=ThemeWidget.foregroundcolor)
        self.welcometext.grid(row=0, column=0,  padx=30,)


#a sub frame to hold the logics
        self.loginsubframe = tk.Frame(self, background=ThemeWidget.homepage_backgroundcolor) 
        self.loginsubframe.grid(row=0, column=1, ipadx=50 )
        


        self.login_label = ttk.Label(self.loginsubframe, text="Log in",foreground=ThemeWidget.signuptextcolor, font=ThemeWidget.signuptextfont, background=ThemeWidget.homepage_backgroundcolor)
        self.login_label.grid(row=0, column=1, ipadx=5)
        
        self.email_label = ttk.Label(self.loginsubframe, text="email", background=ThemeWidget.homepage_backgroundcolor, font=ThemeWidget.generalfont, foreground=ThemeWidget.foregroundcolor)
        self.email_label.grid(row=1, column=0)


        self.email_entry = ttk.Entry(self.loginsubframe)
        self.email_entry.grid(row=1, column=1, pady=10, padx=5)

        self.password_label = ttk.Label(self.loginsubframe,text="Password", font=ThemeWidget.generalfont, foreground=ThemeWidget.foregroundcolor, background=ThemeWidget.homepage_backgroundcolor)
        self.password_label.grid(row=2, column=0)

        self.password_entry = ttk.Entry(self.loginsubframe)
        self.password_entry.grid(row=2, column=1, padx=5, pady=10)



        self.login_button = tk.Button(self.loginsubframe, text="Login", command=self.is_login_success, background=ThemeWidget.sigupbg, foreground=ThemeWidget.foregroundcolor)

        self.login_button.grid(row=3, column=1, ipadx=50, pady=20)

    def is_login_success(self):
        
        self.password = self.password_entry.get()

        try:
            if self.email_validation() and self.password:
                self.checklogindata = FirebaseRestApi()
                token = self.checklogindata.authentication().sign_in_with_email_and_password(email=self.email, password=self.password)
                
                
                
                keyring.set_password(service_name="firebase",
                                     username="token",
                                       password=token.get("idToken").encode("utf-8"))
            
                
                messagebox.showinfo(title="Logic in", message="Login Successfully")
                self.controller.show_frames(HomeScreen)

        except  HTTPError as e:
            errmessage = e.args[1]
            error_data = json.loads(errmessage)
            if error_data["error"]["message"] == "CONFIGURATION_NOT_FOUND":
                messagebox.showerror("", message="User Info not Found")
            elif error_data["error"]["message"] == "INVALID_EMAIL":
                messagebox.showerror(title="", message="Invalid email")
            else:
                messagebox.showerror("", message="details invalid")
        except socket.gaierror:
            messagebox.showerror("internet", message="could not connect")
        except ConnectionError:
            messagebox.showerror("", "Connection error.. try again")
        except requests.exceptions.ConnectionError:
            messagebox.showerror("", "No Internet")
        except requests.exceptions.HTTPError:
            messagebox.showerror("", "Connection Error")
        except Exception as e:
            messagebox.showerror("", message=e)
            



    def email_validation(self):
        self.email = self.email_entry.get()

        try:
            self.new_email = email_validator.validate_email(self.email, check_deliverability=True)
            return self.new_email.normalized
        except email_validator.EmailSyntaxError as e:

            messagebox.showerror(title="Invalid", message=e)
        
        except email_validator.EmailNotValidError as e:

            messagebox.showerror(title="Invalid", message=e)
        except email_validator.EmailUndeliverableError as e:

            messagebox.showerror(title="Invalid", message=e)

       
        






        

        