import math


def addition (x,y):
  return x + y
def subtraction (x,y):
  return x - y
def multiply (x,y):
  return x*y
def division (x, y):
    if y == 0:
        return "Error"
    return x / y
def factorial (x):
    if x == 0:
        return 1
    else:
        return x*factorial(x-1)
def xPowery (x,y):
    return x**y
def log(x,y):
    return math.log(x,y)
def ln (x):
    return math.log(float(x))
def menu():
  user_input = int(0)
  while (user_input != 9):
    print("1. Addition\n2. Subtraction\n3. Multiply\n4. Divide\n5. Factorial\n6. X Power Y\n7. Log\n8. Natural Log\n9. Quit")
    user_input=int(input("Enter your Choice:"))
    if user_input == 1:
        input1 = int(input("Enter First Number: "))
        input2 = int(input("Enter Second Number: "))
        print(addition(input1,input2))
    elif user_input == 2:
        input1 = int(input("Enter First Number: "))
        input2 = int(input("Enter Second Number: "))
        print(subtraction(input1,input2))
    elif user_input == 3:
        input1 = int(input("Enter First Number: "))
        input2 = int(input("Enter Second Number: "))
        print(multiply(input1,input2))
    elif user_input == 4:
        input1 = int(input("Enter First Number: "))
        input2 = int(input("Enter Second Number: "))
        print(division(input1,input2))
    elif user_input == 5:
        input1 = int(input("Enter First Number: "))
        print(factorial(input1))
    elif user_input == 6:
        input1 = int(input("Enter First Number: "))
        input2 = int(input("Enter Second Number: "))
        print(xPowery(input1,input2))
    elif user_input == 7:
        input1 = int(input("Enter First Number: "))
        input2 = int(input("Enter Second Number: "))
        print(log(input1,input2))
    elif user_input == 8:
        input1 = int(input("Enter First Number: "))
        print(ln(input1))
    elif user_input == 9:
        return
menu()
