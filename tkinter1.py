
#Calendar using python tiknter 


import tkinter 
import tkcalendar
from tkinter import *
from tkcalendar import Calendar

root=Tk()
root.title("Calendar")
root.geometry("400x400" )
root['background']='#856ff8'

def grad_date():
    date1.config(text = "Selected Date is: " + cal.get_date())


cal = Calendar(root,selectmode='day',month=6,year=2022,day = 22)
cal.pack(pady=30)



Button(root,text="Date",bg="yellow",command=grad_date).pack(pady=20)
date1= Label(root,text='')
date1.pack(pady=30)
root.mainloop()