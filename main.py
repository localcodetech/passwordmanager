
import tkinter as tk
from app.ui.signup_page import SignupScreen
from app.utils.apptheme import ThemeWidget
# from app.ui.login_page import LogicScreen

class MyMainApp(tk.Tk):
    def __init__(self, screenName = None, baseName = None, className = "Tk", useTk = True, sync = False, use = None):
        super().__init__(screenName, baseName, className, useTk, sync, use)

        self.root = tk.Tk
        self.root.title(self,"vaultlane")
        self.root.geometry(self,"1500x1500")
        self.root.configure(self, bg=ThemeWidget.backgroundcolor)

        self.start_app()



    

    def start_app(self):
        # self.loginpage = LogicScreen(self, self.signup_success)
        # self.loginpage.pack(expand=1, fill="both")


        self.nextpage = SignupScreen(self,self.signup_success)
        self.nextpage.pack(expand=1,anchor="center")


    
    def signup_success(self):

        self.nextpage.destroy()

        self.nn = tk.Label(self, text="done")
        self.nn.pack(padx=50, pady=50)




        

    

          







if __name__ == "__main__":
    app = MyMainApp()
    app.mainloop()

