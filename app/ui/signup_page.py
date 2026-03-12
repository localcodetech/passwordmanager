

import phonenumbers


from email_validator import validate_email
from email_validator import EmailNotValidError,EmailUndeliverableError, EmailSyntaxError


import tkinter as tk
from tkinter import ttk, messagebox
from ..utils.apptheme import ThemeWidget


class SignupScreen(tk.Frame):

    def __init__(self, parent, signup_success ):
        self.signupdone = signup_success
        
        super().__init__(parent)
       

        tk.Frame.configure(self, bg=ThemeWidget.backgroundcolor)

        self.signup_label = tk.Label(self, text="Sign UP", bg=ThemeWidget.backgroundcolor, font=ThemeWidget.signuptextfont, foreground=ThemeWidget.signuptextcolor)
        self.signup_label.grid(row=0, column=1, columnspan=2, pady=10 )

        self.username_label = tk.Label(self, text="Username", bg=ThemeWidget.backgroundcolor, font=ThemeWidget.generalfont, foreground=ThemeWidget.foregroundcolor )
        self.username_label.grid(row=1, column=0)

        self.username_entry = tk.Entry(self, )
        self.username_entry.grid(row=1, column=1, pady=10)

        self.email_label = tk.Label(self, text="Email", bg=ThemeWidget.backgroundcolor, foreground=ThemeWidget.foregroundcolor, font=ThemeWidget.generalfont)
        self.email_label.grid(row=2, column=0)

        self.email_entry = tk.Entry(self)
        self.email_entry.grid(row=2, column=1, pady=10)

        self.phonenumber_label = tk.Label(self, text="Phone", bg=ThemeWidget.backgroundcolor, foreground=ThemeWidget.foregroundcolor, font=ThemeWidget.generalfont)
        self.phonenumber_label.grid(row=3, column=0)

        self.phonenumber_entry = tk.Entry(self)
        self.phonenumber_entry.grid(row=3, column=1, pady=10)
        
        self.password_label = tk.Label(self, text="Password", bg=ThemeWidget.backgroundcolor, foreground=ThemeWidget.foregroundcolor, font=ThemeWidget.generalfont)
        self.password_label.grid(row=4, column=0)

        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.grid(row=4, column=1, pady=10)

        self.signupButton = tk.Button(self, text="Sign up",bg=ThemeWidget.sigupbg, foreground=ThemeWidget.signuptextcolor, command=self.data_validator)
        self.signupButton.grid(row=5, column=1, columnspan=2, pady=20)


        self.account_already_Labelframe = tk.LabelFrame(self,bg="#ffffff", text=" Already has Acoount ? ", labelanchor="n")
        self.account_already_Labelframe.grid(row=7, column=1,ipady=1, ipadx=90, pady=5)
       

        self.account_already_button = tk.Button(self.account_already_Labelframe, text="Sign in here", background=ThemeWidget.backgroundcolor, foreground=ThemeWidget.foregroundcolor, command="")
        self.account_already_button.pack(pady=5)
        



    def data_validator(self):
        self.username = self.username_entry.get().strip()
        self.phone = self.phonenumber_entry.get().strip()
        self.email = self.email_entry.get().strip()
        self.password = self.password_entry.get()



        


        if self.username and self.password and self.validate_email() and self.validate_phonenumber():
            messagebox.showinfo(title="", message="sign up succussfully")

            self.signupdone()

        else:
            messagebox.showwarning("", "error try again")

    def has_account_already(self):
        pass







    def validate_email(self):

        try:
            self.valid_email = validate_email(self.email, check_deliverability=True)

            return self.valid_email.normalized
        
        except EmailSyntaxError as e:

            messagebox.showerror(title="Invalid", message=e)
        
        except EmailNotValidError as e:

            messagebox.showerror(title="Invalid", message=e)
        except EmailUndeliverableError as e:

            messagebox.showerror(title="Invalid", message=e)









    def validate_phonenumber(self):
      
        self.phonevalidate = phonenumbers.parse(self.phone, region="GH")

        if not phonenumbers.is_valid_number(self.phonevalidate):
            messagebox.showerror(title="Error", message="invalid Phone Number")
        else:
            self.valid_phonenumber = phonenumbers.format_number(self.phonevalidate, phonenumbers.PhoneNumberFormat.E164)

            return self.valid_phonenumber


            


        
        
