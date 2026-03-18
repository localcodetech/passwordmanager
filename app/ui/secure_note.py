
import tkinter as tk


from app.utils.apptheme import ThemeWidget




class SecureNote(tk.Frame):
    def __init__(self, root, controller):
        super().__init__(root, background=ThemeWidget.homepage_backgroundcolor)
        self.controller = controller
        self.pack(expand=1, fill="both")


        self.sub_frame = tk.Frame(master=self, height=800, width=1500, relief="flat",background=ThemeWidget.foregroundcolor)
        self.sub_frame.pack(anchor="center", pady=80)

#goto home screen
        from app.ui.home_page import HomeScreen
        self.go_to_homepage = tk.Button(self,command=lambda: self.controller.show_frames(HomeScreen) ,text="Home Screen",activebackground=ThemeWidget.foregroundcolor,width=20, anchor="w",background=ThemeWidget.homepage_backgroundcolor, foreground=ThemeWidget.signuptextcolor, font=("arial",15, "bold"), relief="flat", highlightthickness=0)
        self.go_to_homepage.place(x=30, y=900)

        self.note_title_label = tk.Label(self, height=1,border=0,text="Title",width=25,highlightthickness=1, font=ThemeWidget.generalfont, background=ThemeWidget.homepage_backgroundcolor, foreground=ThemeWidget.foregroundcolor)
        self.note_title_label.pack(pady=40)

        self.note_title_entry = tk.Entry(self, width=30,background=ThemeWidget.foregroundcolor, relief="groove")
        self.note_title_entry.pack(pady=20)

        self.note_content_label = tk.Label(self, height=1,border=0,foreground=ThemeWidget.foregroundcolor,background=ThemeWidget.homepage_backgroundcolor,text="Content",width=25, font=ThemeWidget.generalfont)
        self.note_content_label.pack(pady=20)

        self.note_content_text_field = tk.Text(self, relief="groove",width=30, height=5, background=ThemeWidget.foregroundcolor)
        self.note_content_text_field.pack()




