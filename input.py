from tkinter import *
import tkinter as tk
from advanced import *
import cx_Oracle as cx
from cx_Oracle import *


def input_screen():
    
    
    root_2 = tk.Tk()

    def ADVANCED(): #calling final screen
        root_2.destroy()
        advanced_view()    

    #oracle connect function
    ##################################################
    def oracle_search(): #sql cursor search query
        pass
    def oracle_add(): #sql cursor to add prisoner data
       pass

    def oracle_release(): #sql cursor to delete prisoner data
        pass
    
    
    e1 = StringVar(root_2)
    e2 = StringVar(root_2)
    relation = IntVar(root_2)
    relation.set(0)
    punishment = IntVar(root_2)
    punishment.set(0)
   

    root_2.title("Prison DataBase")
    root_2.resizable(False,False)
    root_2.iconphoto(False,tk.PhotoImage(file='logo1.png'))
    root_2.configure(bg='black')
    root_2.attributes('-alpha',0.85)

    Label(root_2, text='First Name',font='Roboto 15',padx=10,fg='green',bg='black').place(x=190,y=100)
    first_name_input = Entry(root_2,textvariable=e1,width=20,font="Sans",borderwidth=6,bg="black",fg='green').place(x=320,y=100)
    Label(root_2,text='Last Name',font='Roboto 15',padx=10,fg='green',bg='black').place(x=190,y=200)
    last_name_input = Entry(root_2,textvariable=e2,width=20,font="Sans",borderwidth=6,bg="black",fg='green').place(x=320,y=200)
    Label(root_2,text='Relationship',font='Roboto 15',padx=10,fg='green',bg='black').place(x=190,y=300)
    Radiobutton(root_2,text="Married",variable=relation,value=1,font='Roboto 12',padx=10,fg='green',bg='black').place(x=320,y=300)
    Radiobutton(root_2,text="Single",variable=relation,value=0,font='Roboto 12',padx=10,fg='green',bg='black').place(x=420,y=300)
    Label(root_2,text='Punishment',font='Roboto 15',padx=10,fg='green',bg='black').place(x=190,y=370)
    Radiobutton(root_2,text="Life Sentence",variable=punishment,value=0,font='Roboto 12',padx=10,fg='green',bg='black').place(x=320,y=370)
    Radiobutton(root_2,text="Death Row",variable=punishment,value=1,font='Roboto 12',padx=10,fg='green',bg='black').place(x=480,y=370)

    submit_button1 = Button(root_2,text="Search Criminal",borderwidth=3,font='Ariel 12 bold',fg='green',bg='black',command=oracle_search).place(x=470,y=500)
    add_button = Button(root_2,text="Add Criminal",borderwidth=3,font='Ariel 12 bold',fg='green',bg='black',command=oracle_add).place(x=350,y=500)
    release_button = Button(root_2,text="Release Criminal",borderwidth=3,font='Ariel 12 bold',fg='green',bg='black',command=oracle_release).place(x=200,y=500)
    Advanced_options = Button(root_2,text="Advanced Options",borderwidth=3,font='Ariel 12 bold',fg='green',bg='black',command=ADVANCED).place(x=640,y=559)
    root_2.geometry('800x600') #lengthxwidth
    root_2.mainloop()




