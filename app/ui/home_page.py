
import tkinter as tk

from app.utils.apptheme import ThemeWidget

class HomeScreen(tk.Frame):
    def __init__(self, master ):

        super().__init__(master)

        tk.Frame.configure(self, bg=ThemeWidget.backgroundcolor)

        self.mainframe = tk.Frame(self,background=ThemeWidget.loginPagebackgroundColor)

        self.mainframe.pack(expand=1, fill="both")

        