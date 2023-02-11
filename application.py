from customtkinter import *
from tkinter import *
from PIL import Image, ImageTk




class application(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("920x600")
        self.resizable(False,False)
        self.label()
    
    def label(self):
        
        self.Image = Image.open("Resources/login_background.jpg")
        self.resizedImage = self.Image.resize((920,600))
        self.backgroundImage = ImageTk.PhotoImage(self.resizedImage)
        self.backgroundImageLabel = Label(self,image=self.backgroundImage)
        self.backgroundImageLabel.place(x=0,y=0)
        
        
