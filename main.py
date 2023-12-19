from Group_work import fibonacci
from mendy import factorial


if __name__ =='__main__':
    print("which task would you like to perform: ")
    print("1: Find the factorial")
    print("2: Find the fibonacci value")
    e = eval(input("Enter the number of the task you'd like to perform: "))

    if e == 1:
        k = eval(input("Enter the integer you'd like like to perform: "))
        print("The factorial of " + str(k) + "is:" + factorial(k))
