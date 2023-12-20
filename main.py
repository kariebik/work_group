from Group_work import fibonacci_sequence
from mendy import factorial

from tkinter import *


root =Tk()
root.title("Milestone 2")
label1 = Label(root, text= "Enter the number of the task you'd like to perform:")

label1.pack()

e = Entry(root)
e.pack()

n = eval(e.get())

button = Button(root, text='Find the factorial', command= lambda: factorial(n))
button2 = Button(root, text='Find the fibonacci', command=lambda: fibonacci_sequence(n))
button.pack()
button2.pack()


root.mainloop()


