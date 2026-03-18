

import tkinter as tk
from app.ui.signup_page import SignupScreen
from app.utils.apptheme import ThemeWidget
from firebase__init__ import FirebaseAdminSDK





class MyMainApp(tk.Tk):
    def __init__(self ):
        super().__init__()
        self.start = FirebaseAdminSDK()

        self.geometry("1500x1500")
        self.title("VaultLane")
        self.configure(background=ThemeWidget.homepage_backgroundcolor)

        self.current_frame = None

        self.show_frames(SignupScreen)



    def show_frames(self, page_class):
        
        if self.current_frame is not None:
            self.current_frame.destroy()

        self.current_frame = page_class(root=self, controller=self)

        
       



if __name__ == "__main__":
    app = MyMainApp()
    app.mainloop()

