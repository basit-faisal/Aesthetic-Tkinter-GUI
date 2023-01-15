from tkinter import *
import tkinter as tk
from input import *

#Window 2 function
############################################################################################################
def new_window():
    root.destroy()
    input_screen()
############################################################################################################


########Initial Screen
root = tk.Tk()
root.title("Prison DataBase")
root.resizable(False,False) 
root.iconphoto(False,tk.PhotoImage(file='logo1.png'))
background_image = tk.PhotoImage(file='a.png')
Label(root,image=background_image).place(x=0,y=0)
root.attributes('-alpha',0.85)

submit_button = Button(root,text='Continue',borderwidth=3,font='Ariel 12 bold',command=new_window,fg='green',bg='black').place(rely=1.0, relx=1.0, x=0, y=0,anchor=SE)

root.geometry('800x600') #lengthxwidth
root.mainloop()


