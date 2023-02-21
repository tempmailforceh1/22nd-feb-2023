from  tkinter import *

reg= Tk()

reg.geometry('500x500')

reg.title("Registration Page")

reg.config(bg="light green")

firstname=Label (reg,text="First name").grid(row=0,column=0)
e1=Entry(reg).grid(row=0,column=1)


lastname=Label(reg,text="Last name").grid(row=1,column=0)
e2=Entry(reg).grid(row=1,column=1)


username=Label(reg,text="Username").grid(row=2,column=0)
e2=Entry(reg).grid(row=2,column=1)



password=Label(reg,text="password").grid(row=3,column=0)
e2=Entry(reg).grid(row=3,column=1)



email=Label(reg,text="email").grid(row=4,column=0)
e2=Entry(reg).grid(row=4,column=1)



address=Label(reg,text="address").grid(row=5,column=0)
e2=Entry(reg).grid(row=5,column=1)

reg=Button(reg,text="Register").grid(row=6,column=1)

 
reg.mainloop()
