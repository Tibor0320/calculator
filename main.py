# Calculator Program
import sys


def add(num1, num2):  # Add
    return num1 + num2

def sub(num1, num2): #Subtract
    return num1 - num2

def mul(num1, num2): # Multiply
    return num1 * num2

def div(num1, num2): # Divide
    return num1 / num2

operations = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div,
    }   # Adding the functions into a dict

# Ask for inputs

def calc():
    accumulate = True

    n1 = float(input("Enter a number: "))

    while accumulate:

        for x in operations:
            print(x) # Showcases the operators
        operator = input("Enter an operator: ")

        if operator not in operations:
            print("Invalid operator")
            sys.exit("Please enter a valid operator")

        n2 = float(input("Enter the second number: "))
        answer = operations[operator](n1, n2)

        print(f"{n1} {operator} {n2} = {answer}")

        # Ask the user if he/she wants to use the prev answer

        choice = input(f"Type 'y' to continue calculation with {answer}, or type 'n' to exit calculation: ")

        if choice == "y":
            n1 = answer
        else:
            accumulate = False
            sys.exit("Bye")

calc()


