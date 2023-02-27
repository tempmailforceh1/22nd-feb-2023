from tkinter import *
from functools import partial

from tkinter import messagebox

tk=Tk()

def validatelogin(username,password):
    print("username entered",username.get())
    print("password entered",password.get())
    return

tk.geometry("400x150")
tk.title("login page")
tk.config(bg="blue")

uname=Label(tk,text="username").grid(row=0,column=0)
username=StringVar()

e1=Entry(tk,textvariable=username).grid(row=0,column=1)


password=Label(tk,text="password").grid(row=1,column=0)
password=StringVar()

e2=Entry(tk,textvariable=password,show="*").grid(row=1,column=1) #show used to hide password
validatelogin=partial(validatelogin,username,password)

submit=Button(tk,text="login",command=validatelogin).grid(row=4,column=0)
tk.mainloop()

