from Group_work import fibonacci_sequence
from mendy import factorial


if __name__ =='__main__':
    print("which task would you like to perform: ")
    print("1: Find the factorial")
    print("2: Find the fibonacci value")
    e = eval(input("Enter the number of the task you'd like to perform: "))

    if e == 1:
        k = eval(input("Enter the integer you'd like like to perform: "))
        if not isinstance(k, int):
            raise TypeError
        print("The factorial of " + str(k) + " is: " + str(factorial(k)))
    elif e == 2:
        n = eval(input("Enter the sequence position of the fibonacci value: "))
        if not isinstance(n, int):
            raise TypeError
        print("The " + str(n) + " th fibonacci is " + str(fibonacci_sequence(n)))
