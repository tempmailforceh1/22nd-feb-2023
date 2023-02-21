#example of GRID method

from  tkinter import *

login = Tk()

login.geometry('500x500')

login.title("Login Page")

login.config(bg="pink")

username=Label (login,text="username").grid(row=0,column=0)
e1=Entry(login).grid(row=0,column=1)


password=Label (login,text="password").grid(row=1,column=0)
e2=Entry(login).grid(row=1,column=1)


login=Button(login,text="login").grid(row=4,column=0)

login.mainloop()
