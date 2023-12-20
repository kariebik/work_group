from Group_work import fibonacci_sequence
from mendy import factorial

from tkinter import *


root =Tk()
root.title("Milestone 2")

label1 = Label(root, text="which task would you like to perform: ").grid(row=0, column=0, columnspan=2)
label2 = Label(root, text="1: Find the factorial").grid(row=1, column=0)
label3 = Label(root, text="2: Find the fibonacci value").grid(row=2, column=0)
label4 = Label(root, text= "Enter the number of the task you'd like to perform:").grid(row=3, column=0)

e = Entry(root).grid(row=3, column=1, columnspan=2)
n = int(e.get())
def command():
    if e.get() == 1:
        label5 = Label(root, text="Enter the integer you'd like like to perform: ").grid(row=4, column=0)
        e2 = Entry(root).grid(row=4, column=1, columnspan=2)
        button = Button(root, text='get results', command= lambda: factorial(e2) )
    elif e.get() == 2:
        label5 = Label(root, text="Enter the sequence position of the fibonacci value: ").grid(row=4, column=0)
        e2 = Entry(root).grid(row=4, column=1, columnspan=2)
        button = Button(root, text='get results', command=lambda: fibonacci_sequence(e2))


root.mainloop()


