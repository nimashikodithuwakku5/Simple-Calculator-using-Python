import re  # Import regex for parsing expressions

# Arithmetic functions
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Division by zero"
    except Exception as e:
        return f"Error: {e}"

def power(a, b):
    return a ** b

def remainder(a, b):
    return a % b

# History storage
history = []

# Function to parse and evaluate expressions like "3+2"
def evaluate_expression(expression):
    # Match pattern for an expression like "3+2", "10/5", etc.
    match = re.fullmatch(r"(-?\d+(?:\.\d+)?)([+\-*/^%])(-?\d+(?:\.\d+)?)", expression)
    if not match:
        return None  # Return None if the expression is invalid
    
    # Extract numbers and operator
    num1, operator, num2 = match.groups()
    num1, num2 = float(num1), float(num2)  # Convert operands to float
    
    # Perform calculation based on the operator
    if operator == '+':
        return add(num1, num2)
    elif operator == '-':
        return subtract(num1, num2)
    elif operator == '*':
        return multiply(num1, num2)
    elif operator == '/':
        return divide(num1, num2)
    elif operator == '^':
        return power(num1, num2)
    elif operator == '%':
        return remainder(num1, num2)
    return None

# Function to handle operations
def select_op(choice):
    if choice == '#':
        return -1
    elif choice == '$':
        history.clear()  # Clear history for reset
        return 0
    elif choice == '?':
        if history:
            for record in history:
                print(record)
        else:
            print("No past calculations to show")
        return 0

    # Check if the input is a direct arithmetic expression
    result = evaluate_expression(choice)
    if result is not None:
        print(result)  # Output only the result
        history.append(result)
        return 0
    
    print("Unrecognized operation")
    return 0

# Main program loop
while True:
    print("\nSelect operation.")
    print("1.Add      : + ")
    print("2.Subtract : - ")
    print("3.Multiply : * ")
    print("4.Divide   : / ")
    print("5.Power    : ^ ")
    print("6.Remainder: % ")
    print("7.Terminate: # ")
    print("8.Reset    : $ ")
    print("9.History  : ? ")
    
    choice = input("Enter choice: ")
    if select_op(choice) == -1:
        break
