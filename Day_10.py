#Calculator Project
import os
from calculator_art import logo

def add(n1,n2):
    return n1+n2

def subtract(n1,n2):
    return n1-n2

def multiply(n1,n2):
    """Multiplies two give integer"""
    return n1*n2

def divide(n1,n2):
    return n1/n2


operator_dictionary = {"+":add,
                       "-":subtract,
                       "*":multiply,
                       "/":divide
                        }

def calculator():
    print(logo) 
    num1 = float(input("What's the first number?: "))
    flag = True
    while flag:
        for key in operator_dictionary:
            print(key)
        operation = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        result = operator_dictionary[operation](num1,num2)
        print(f"{num1} {operation} {num2} = {result}")
        num1 = result
        y_n = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start new calculation: ")
        if y_n == "n":
            flag = False
            os.system('cls')
            calculator()
calculator()
