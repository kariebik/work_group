
from tkinter import *


root =Tk()
root.title("Milestone 2")
label1 = Label(root, text= "Enter the number of the task you'd like to perform:")


def fibonacci_sequence(n):
    n = int(n)
    """
#     Return the value in the fibonacci sequence at point n.
#     Example fibonacci_sequence(8) = 34
#     :param n: int
#     :return: int
#     """
    first_val = 1
    second_val = 1
    total = 0
    for n in range(1, n):
        total = first_val + second_val
        third_val = first_val + second_val
        first_val = second_val
        second_val = third_val
    label = Label(root, text=total)
    label.pack()


import math

def factorial(k):
    k = int(k)
    """
    Return the factorial of the integer k.
    Example: factorial(3) = 1 * 2 * 3 = 6
    :param k: int
    :return: int
    """
    if k < 0:
        raise TypeError
    elif k == 0 or k == 1:
        label = Label(root, text='1')
    else:
        label = Label(root, text=math.factorial(k))
    label.pack()


label1.pack()

e = Entry(root)
e.pack()



button = Button(root, text='Find the factorial', command= lambda: factorial(e.get()))
button2 = Button(root, text='Find the fibonacci', command= lambda: fibonacci_sequence(e.get()))
button.pack()
button2.pack()


root.mainloop()


