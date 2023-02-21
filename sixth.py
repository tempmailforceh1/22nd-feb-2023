from  tkinter import *

top= Tk()

top.geometry('500x500')

top.title("Registration Page")

top.config(bg="light green")


name=Label (top,text="Name").place(x=30,y=50)
email=Label (top,text="Email").place(x=30,y=90)
password=Label (top,text="Password").place(x=30,y=120)


e1=Entry(top).place(x=80,y=50)

e2=Entry(top).place(x=80,y=90)

e3=Entry(top).place(x=80,y=120)

submit=Button(top,text="submit").place(x=30,y=160)

top.mainloop()
