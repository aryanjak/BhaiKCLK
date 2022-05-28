from tkinter import *
from tkinter.ttk import *
from time import strftime
from datetime import datetime as dt

def samay():
    t = dt.now().strftime('%H %M %S.%f: %p')
    lable.config(text = t)
    lable.after(1000 , samay)

root = Tk()
root.title("Ghaडी")
lable = Label(root , font=("ds-digital" , 80) , background="black" , foreground="green")
lable.pack(anchor = "center")
samay()

root.mainloop()