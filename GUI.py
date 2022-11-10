from msilib.schema import CheckBox
from tkinter import *
import tkinter as tk
import os
from urllib.robotparser import RobotFileParser
from database.migration import migration
from main import checkFromListBM, checkFromListCM, result, sell
root = tk.Tk()
def menu():
    
    
    def CheckPrice():
        button1.destroy()
        button2.destroy()
        button3.destroy()
        button4.destroy()
        def back():
            backButton.destroy()
            resButton.destroy()
            cmButton.destroy()
            bmButton.destroy()
            menu()
        backButton = Button(root,text="Back", font=("Comic Sans", 30, 'bold'), fg="#0eb519", bg="#000000", activebackground="#000000",activeforeground="#0eb519", width=20, command=back)
        backButton.grid(row=0,column=0)
        resButton = Button(root,text="RESULT", font=("Comic Sans", 30, 'bold'), fg="#0eb519", bg="#000000", activebackground="#000000",activeforeground="#0eb519", width=20, command=result)
        resButton.grid(row=0,column=1)
        cmButton = Button(root,text="CAERLEON MARKET", font=("Comic Sans", 30, 'bold'), fg="#0eb519", bg="#000000", activebackground="#000000",activeforeground="#0eb519", width=20, command=checkFromListCM)
        cmButton.grid(row=1,column=0)
        bmButton = Button(root,text="BLACK MARKET", font=("Comic Sans", 30, 'bold'), fg="#0eb519", bg="#000000", activebackground="#000000",activeforeground="#0eb519", width=20, command=checkFromListBM)
        bmButton.grid(row=1,column=1)
    
    def sellPage():
        button1.destroy()
        button2.destroy()
        button3.destroy()
        button4.destroy()
        def back():
            bacButton.destroy()
            e.destroy()
            label.destroy()
            menu()
            
        bacButton = Button(root,text="Back", font=("Comic Sans", 30, 'bold'), fg="#0eb519", bg="#000000", activebackground="#000000",activeforeground="#0eb519", width=10, command=back)
        bacButton.grid(row=0,column=0)
        label = tk.Label(root, text="amount:",font=("Comic Sans", 30, 'bold'), fg="#0eb519", bg="#000000", activebackground="#000000",activeforeground="#0eb519", width=10)
        label.grid(row=1, column=0)
        e = tk.Entry(root, font=("Comic Sans", 30, 'bold'), fg="#0eb519", bg="#000000", width=10)
        e.grid(row=1,column=1)
        sellButton = Button(root,text="Sell", font=("Comic Sans", 30, 'bold'), fg="#0eb519", bg="#000000", activebackground="#000000",activeforeground="#0eb519", width=10, command=sell)
        sellButton.grid(row=0,column=1)
        
        
    button1 = Button(root,text="Check Price", font=("Comic Sans", 30, 'bold'), fg="#0eb519", bg="#000000", activebackground="#000000",activeforeground="#0eb519", width=20, command=CheckPrice)
    button1.grid(row=0,column=0)


    button2 = Button(root,text="Profit Calculator", font=("Comic Sans", 30, 'bold'), fg="#0eb519", bg="#000000", activebackground="#000000",activeforeground="#0eb519", width=20, command=sellPage)
    button2.grid(row=0,column=1)


    """button3 = Button(root,text="Selling Bot", font=("Comic Sans", 30, 'bold'), fg="#0eb519", bg="#000000", activebackground="#000000",activeforeground="#0eb519", width=15)
    button3.grid(row=1,column=0)"""
    
    button3 = Button(root,text="reset", font=("Comic Sans", 30, 'bold'), fg="#0eb519", bg="#000000", activebackground="#000000",activeforeground="#0eb519", width=20, command=migration)
    button3.grid(row=1,column=0)


    button4 = Button(root,text="Exit", font=("Comic Sans", 30, 'bold'), fg="#0eb519", bg="#000000", activebackground="#000000",activeforeground="#0eb519", width=20, command=exit)
    button4.grid(row=1,column=1)

menu()
root.mainloop()

