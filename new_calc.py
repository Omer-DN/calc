# Program make a simple calculator
import time


# This function adds two numbers
def add(x, y):
    return x + y


# This function subtracts two numbers
def subtract(x, y):
    return x - y


# This function multiplies two numbers
def multiply(x, y):
    return x * y


# This function divides two numbers
def divide(x, y):
    y = checkDivByZero(y)
    return x / y


def check_operation(choose):
    while int(choose) > 4 or int(choose) < 1:
        print('Operation is not defined\n'
              'choose between 1 to 4')
        print('1.Add\n2.Subtract\n3.Multiply\n4.Divide')
        choose = input()
    return choose


def checkDivByZero(number_2):
    while number_2 == 0:
        print("Can't Div by zero")
        number_2 = input('Enter the second number again: ')
    return number_2


def enterNumber():
    num = 0
    while True:
        try:
            num = input()
            num = int(num)

        except ValueError:
            print('ValueError\n\nEnter a number: ', end='')
        else:
            return num


while True:
    print('Enter first number: ', end='')
    num1 = int(enterNumber())
    print('Enter second number: ', end='')
    num2 = int(enterNumber())
    print("Select operation.")
    print('1.Add\n2.Subtract\n3.Multiply\n4.Divide')
    char = input()

    while int(char) > 4 or int(char) < 1:
        print('Operation is not defined\n'
              'choose between 1 to 4')
        print('1.Add\n2.Subtract\n3.Multiply\n4.Divide')
        char = input()

    if char == '1':
        print(num1, "+", num2, "=", add(num1, num2), '\n')

    elif char == '2':
        print(num1, "-", num2, "=", subtract(num1, num2), '\n')

    elif char == '3':
        print(num1, "*", num2, "=", multiply(num1, num2), '\n')

    elif char == '4':
        print(num1, "/", num2, "=", divide(num1, num2), '\n')

    # check if user wants another calculation
    # break the while loop if answer is no
    next_calculation = input("Let's do next calculation? (yes/no): ")
    if next_calculation == "no":
        exit()
