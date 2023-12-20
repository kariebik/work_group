import math
from tkinter import *
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
        label = Label(root, text= '1')
    else:
        label = Label(root, text=math.factorial(k))
    label.pack()