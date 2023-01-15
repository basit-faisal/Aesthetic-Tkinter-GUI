from tkinter import *
import tkinter as tk
from tkinter import ttk
from treedisplay_adv import *



def advanced_view():
    
    root_3 = tk.Tk()
    root_3.title("Prison DataBase")
    root_3.resizable(False,False)
    root_3.iconphoto(False,tk.PhotoImage(file='logo.png'))
    root_3.configure(bg='black')
    root_3.attributes('-alpha',0.85)

    def tree_window(selector):
        root_3.destroy()
        tableview(selector)  

    common_var = IntVar(root_3)
    

    Radiobutton(root_3,text="Show All Prisoners",variable=common_var,value=1,font='Roboto 12',padx=10,fg='green',bg='black').place(x=320,y=70)
    Radiobutton(root_3,text="Show Male Prisoners",variable=common_var,value=2,font='Roboto 12',padx=10,fg='green',bg='black').place(x=320,y=100)
    Radiobutton(root_3,text="Show Female Prisoners",variable=common_var,value=3,font='Roboto 12',padx=10,fg='green',bg='black').place(x=320,y=130)
    Radiobutton(root_3,text="Total Prisoners",variable=common_var,value=4,font='Roboto 12',padx=10,fg='green',bg='black').place(x=320,y=160)
    Radiobutton(root_3,text="Prisoners below age 20",variable=common_var,value=5,font='Roboto 12',padx=10,fg='green',bg='black').place(x=320,y=260)
    Radiobutton(root_3,text="Prisoners below age 40",variable=common_var,value=6,font='Roboto 12',padx=10,fg='green',bg='black').place(x=320,y=290)
    Radiobutton(root_3,text="Prisoners below age 60",variable=common_var,value=7,font='Roboto 12',padx=10,fg='green',bg='black').place(x=320,y=320)
    Radiobutton(root_3,text="Prisoners from Punjab",variable=common_var,value=8,font='Roboto 12',padx=10,fg='green',bg='black').place(x=320,y=420)
    Radiobutton(root_3,text="Prisoners from KPK",variable=common_var,value=9,font='Roboto 12',padx=10,fg='green',bg='black').place(x=320,y=450)
    Radiobutton(root_3,text="Prisoners from Sindh",variable=common_var,value=10,font='Roboto 12',padx=10,fg='green',bg='black').place(x=320,y=480)
    Radiobutton(root_3,text="Prisoners from Balochistan",variable=common_var,value=11,font='Roboto 12',padx=10,fg='green',bg='black').place(x=320,y=510)

    execute_button = Button(root_3,text='Execute & Close',borderwidth=3,font='Ariel 12 bold',command=lambda:tree_window(common_var),fg='green',bg='black')
    execute_button.place(x=650,y=560)
    root_3.geometry('800x600') #lengthxwidth
    root_3.mainloop()


#advanced_view()
