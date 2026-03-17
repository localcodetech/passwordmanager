
import tkinter as tk

from app.utils.apptheme import ThemeWidget



class PasswordDashboard(tk.Frame):
    def __init__(self, root, controller):
        super().__init__(root, background=ThemeWidget.homepage_backgroundcolor)
        self.controller = controller


        tk.Frame.configure(bg="#ffffff")


