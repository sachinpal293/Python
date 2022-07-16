# def greet(name,time):
#     print(f"Good {time}, {name}")
#
# name = input("enter your name : ")
# time = input("enter your time : ")
# greet(name,time)
#


# Take something and return something



def sum(num1,num2=0,num3=0):
    return num1+num2+num3

num1 = 10
num2 = 87
add = sum(num1,52)
print("sum of num1 and num2 is ",add)
# print("Sum of num1 and num2 is ",sum(num1,num2))


# take nothing return something
def factorial():
    """This is Docstring"""
    num = int(input("enter a number : "))
    fac = 1
    while(num>0):
        fac = fac*num
        num -=1

    return fac


print(factorial.__doc__)

