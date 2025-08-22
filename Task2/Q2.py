import math

def add(a, b): return a + b
def sub(a, b): return a - b
def mul(a, b): return a * b
def div(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Division by zero"
def mod(a, b):
    try:
        return a % b
    except ZeroDivisionError:
        return "Error: Modulo by zero"
def power(a, b): return a ** b
def factorial(a):
    if a < 0: return "Error: Negative factorial not defined"
    return math.factorial(a)

def calculator():
    print("Operations: +, -, *, /, %, **, ! (factorial)")
    while True:
        op = input("\nEnter operation (or 'exit'): ")
        if op == "exit":
            break
        if op == "!":
            n = int(input("Enter number: "))
            print("Result:", factorial(n))
        else:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            if op == "+": print("Result:", add(a, b))
            elif op == "-": print("Result:", sub(a, b))
            elif op == "*": print("Result:", mul(a, b))
            elif op == "/": print("Result:", div(a, b))
            elif op == "%": print("Result:", mod(a, b))
            elif op == "**": print("Result:", power(a, b))
            else: print("Invalid operation")

calculator()
