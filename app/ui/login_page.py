


import tkinter as tk
from tkinter import messagebox, ttk

from app.utils.apptheme import ThemeWidget

class LogicScreen(tk.Frame):
    def __init__(self,  master,signup_success ):  
        super().__init__(master)
        
        self.signup_done = signup_success

        tk.Frame.configure(self, background=ThemeWidget.loginPagebackgroundColor)
        tk.Frame.columnconfigure(self, 0, weight=1)
        tk.Frame.columnconfigure(self,1, weight=1)
        tk.Frame.rowconfigure(self, 0, weight=1)
        
      
        self.welcometext = ttk.Label(self, text="Welcome Back",font=ThemeWidget.welcome_font, background=ThemeWidget.loginPagebackgroundColor, foreground=ThemeWidget.foregroundcolor)
        self.welcometext.grid(row=0, column=0,  padx=30,)


#a sub frame to hold the logics
        self.loginsubframe = tk.Frame(self, background=ThemeWidget.loginPagebackgroundColor) 
        self.loginsubframe.grid(row=0, column=1, ipadx=50 )
        


        self.login_label = ttk.Label(self.loginsubframe, text="Log in",foreground=ThemeWidget.signuptextcolor, font=ThemeWidget.signuptextfont, background=ThemeWidget.loginPagebackgroundColor)
        self.login_label.grid(row=0, column=1, ipadx=5)
        
        self.username_label = ttk.Label(self.loginsubframe, text="username", background=ThemeWidget.loginPagebackgroundColor, font=ThemeWidget.generalfont, foreground=ThemeWidget.foregroundcolor)
        self.username_label.grid(row=1, column=0)


        self.username_entry = ttk.Entry(self.loginsubframe)
        self.username_entry.grid(row=1, column=1, pady=10, padx=5)

        self.password_label = ttk.Label(self.loginsubframe,text="Password", font=ThemeWidget.generalfont, foreground=ThemeWidget.foregroundcolor, background=ThemeWidget.loginPagebackgroundColor)
        self.password_label.grid(row=2, column=0)

        self.password_entry = ttk.Entry(self.loginsubframe)
        self.password_entry.grid(row=2, column=1, padx=5, pady=10)



        self.login_button = tk.Button(self.loginsubframe, text="Login", command=self.is_login_success, background=ThemeWidget.sigupbg, foreground=ThemeWidget.foregroundcolor)

        self.login_button.grid(row=3, column=1, ipadx=50, pady=20)

    def is_login_success(self):
        self.username = self.username_entry.get()
        self.password = self.password_entry.get()


        if self.username and self.password:
            messagebox.showinfo(title="Logic in", message="data done")

            self.signup_done()



        else:
            messagebox.showerror(title="error", message="could not login")







        

        