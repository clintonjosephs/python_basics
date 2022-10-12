# validations
def validate(num1, num2):
    if (len(num1) == 0 or len(num2) == 0):
        print("Please enter numbers")
        exit()
    try:
        num1 = float(num1)
        num2 = float(num2)
        return num1, num2
    except ValueError:
        print("Only numbers and decimals allowed")
        exit()

# basic arithmetic operations
def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

# collect input from user
def collect_input():
    num1 = input("Enter the first number: ")
    num2 = input("Enter the second number: ")
    first, second = validate(num1, num2)
    return first, second

def choose_operation():
    operation = input("""Choose an operation:
    1. Addition
    2. Subtraction
    3. Multiplication
    4. Division
    """)
    if operation == "1":
        return add
    elif operation == "2":
        return subtract
    elif operation == "3":
        return multiply
    elif operation == "4":
        return divide
    else:
        print("Invalid operation")
        exit()

# call main function
def main():
    num1, num2 = collect_input()
    operation = choose_operation()
    result = operation(num1, num2)
    print(result)

if __name__ == "__main__":
    main()
