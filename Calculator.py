def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


print("This is a simple calculator")


while True:
    try:
        number1 = int(input("Type first number:"))
        break
    except:
        print("Please type a number:")


while True:
    try:
        number2 = int(input("Type second number:"))
        break
    except:
        print("Please type a number:")

while True:
    function = input("Choose operations (+, -, *, / or type: add, subtract, multiply, divide):")

    if function == "add" or function == "Add" or function == "+":
        print("Result:", add(number1, number2))
        break

    if function == "subtract" or function == "Subtract" or function == "-":
        print("Result:", subtract(number1, number2))
        break

    if function == "multiply" or function == "Multiply" or function == "*":
        print("Result:", multiply(number1, number2))
        break

    if function == "divide" or function == "Divide" or function == "/":
        print("Result:", divide(number1, number2))
        break

    else:
        print("Wrong input please try again!")
