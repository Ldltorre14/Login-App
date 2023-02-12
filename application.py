from customtkinter import *
from customtkinter import CTkBaseClass
from tkinter import *
import tkinter.ttk as ttk
from PIL import Image, ImageTk




class application(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("920x600")
        self.resizable(False,False)
        self.configure(bg='#E9F9F6')
        self.label()
    
    def label(self):
        #Background Image setting
        self.Image = Image.open("Resources/login_background.jpg")
        self.resizedImage = self.Image.resize((920,600))
        self.backgroundImage = ImageTk.PhotoImage(self.resizedImage)
        self.backgroundImageLabel = Label(self,image=self.backgroundImage)
        self.backgroundImageLabel.place(x=0,y=0)
        
        #Frame setting
        self.frm = CTkFrame(self,
                            width=400,
                            height=450,
                            fg_color='#E9F9F6',
                            bg_color='#E9F9F6',
                            )
        self.frm.place(x=260,y=80)
        
        #Entry-data Label setting
        self.userLabel = CTkLabel(self.frm,
                                  text="Username", 
                                  font=("Open Sans", 16),
                                  fg_color='white',
                                  corner_radius=20) 
        self.userLabel.place(x=60,y=180)
        self.passwordLabel = CTkLabel(self.frm,
                                      text="Password",
                                      font=("Open Sans", 16),
                                      fg_color='white',
                                      corner_radius=20)
        self.passwordLabel.place(x=60,y=230)
        
        
        
        
