
import tkinter as tk

window=tk.Tk()
#tk.config('300x450')

frame1=tk.Frame(master=window,width=100,height=100,bg="red")
frame1.pack(fill=tk.X)


frame2=tk.Frame(master=window,width=100,height=100,bg="white")
frame2.pack(fill=tk.X)


frame3=tk.Frame(master=window,width=100,height=100,bg="green")
frame3.pack(fill=tk.X)

tk.mainloop()
