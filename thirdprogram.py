#example of pack method

from  tkinter import *

tk = Tk()

tk.title(" Welcome Sri Indu Students")

tk.geometry('500x500')

tk.config(bg="lavender")
#pack method design the window left,right,top,bottom
redbuttton=Button(tk,text="redbutton",fg="red").pack(side="left")

bluebutton=Button(tk,text="bluebutton",fg="blue").pack(side="right")

greenbutton=Button(tk,text="greenbutton",fg="green").pack(side="top")

pinkbutton=Button(tk,text="pinkbutton",fg="pink").pack(side="bottom")

tk.mainloop()
