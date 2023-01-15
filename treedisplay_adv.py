from tkinter import *
import tkinter as tk
from tkinter import ttk
        
        
        
        
def tableview(var): 
    save = var
    root_4 = Tk()
    root_4.title("Prison DataBase")
    root_4.resizable(False,False)
    root_4.iconphoto(False,tk.PhotoImage(file='logo.png'))
    root_4.configure(bg='black')
    root_4.attributes('-alpha',0.85)

    col = ("name","id")
    tv = ttk.Treeview(root_4,height=40,show='headings',columns=col)
    
    tv.column('name',width=100,anchor=CENTER)
    tv.column('id',width=100,anchor=CENTER)

    tv.heading('name',text='Name')
    tv.heading('id',text='id')
   
    tv.pack(side=TOP,fill=BOTH)

    NAME = ['ab','al','sh','as','ass','we','wq','rr','ty','vc']
    id = [1,2,3,4,5,6,7,8,9,10]

    for i in range(10):
        tv.insert('',i,values=(NAME[i],id[i]))

    root_4.geometry('800x600')
    root_4.mainloop()
