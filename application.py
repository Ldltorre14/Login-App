from customtkinter import *
from customtkinter import CTkBaseClass
from tkinter import *
from tkinter import messagebox
import tkinter.ttk as ttk
from PIL import Image, ImageTk




class application(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("920x600")
        self.resizable(False,False)
        self.configure(bg='#E9F9F6')
        self.label()
        self.entry()
        self.button()
    
    def login(self):
        #We store the user entry 
        correctEmail = "lopdlt14@gmail.com"
        correctPassword = "Haxorus12"
        password = self.passwordEntry.get()
        email = self.emailEntry.get()
        
        #We make the validations to see if the credentials are correct, wrong or missing
        if password == correctPassword and email == correctEmail:
            messagebox.showinfo("LOGIN","You Logged in Succesfully")
        elif self.emailEntry.get() == "" or self.passwordEntry.get() == "":
            messagebox.showwarning("LOGIN","Missing info")
        else:
            messagebox.showerror("LOGIN", "Credentials are incorrect")
    
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
        
        #Title Label
        self.titleLabel = CTkLabel(self.frm,
                                   text="Log In",
                                   font=("Open Sans", 40),
                                   )
        self.titleLabel.place(x=145,y=50)
        
        #Entry-data Label setting
        self.emailLabel = CTkLabel(self.frm,
                                  text="Email", 
                                  font=("Open Sans", 16),
                                  fg_color='#CFB5FF',
                                  text_color='black',
                                  corner_radius=20) 
        self.emailLabel.place(x=60,y=180)
        self.passwordLabel = CTkLabel(self.frm,
                                      text="Password",
                                      font=("Open Sans", 16),
                                      fg_color='#CFB5FF',
                                      text_color='black',
                                      corner_radius=20)
        self.passwordLabel.place(x=60,y=230)
        
        
    def entry(self):
        #entry setting
        self.emailEntry = CTkEntry(self.frm,
                                      height=20,
                                      width=200,
                                      placeholder_text="Email*",
                                      placeholder_text_color='grey')
        self.emailEntry.place(x=180,y=183)
        
        self.passwordEntry = CTkEntry(self.frm,
                                      height=20,
                                      width=200,
                                      placeholder_text="Password*",
                                      placeholder_text_color='grey',
                                      show='*')
        self.passwordEntry.place(x=180,y=233)
        
    def button(self):
        self.loginButton = CTkButton(self.frm,
                                     text="LOGIN",
                                     text_color="white",
                                     hover=True,
                                     hover_color='black',
                                     command=self.login
                                     )
        self.loginButton.place(x=135,y=350)
