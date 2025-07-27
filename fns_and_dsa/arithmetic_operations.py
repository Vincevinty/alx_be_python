# A function that performs a basic arithmetic operations.
def perform_operation(num1: float, num2: float, operation: str):
    """the function should execute arithmetic operations
    
    agrs:
        num1 (float): The first number for the operation
        num2 (float): The second number for the operation
        operation (str): The operation parameters accepts four possible values, 'add', 'subtract', 'multiply', or 'divide' """

# Prompt user to enter first number and second number.    
num1 = float(input("Enter first number: "))
num2 = float(input("Enter the second number: "))

# Peform operations based on the user input for first and second number.
operation = input("choose operation ('add', 'subtract', 'multiply',or 'divide'): ").lower()

# Conditional calculation using if,elif or else.
if operation == "add":
    result = num1 + num2
    print(f"The result of adding is: {result}")
    

elif operation == "Subtract":
    result = num1 - num2
    print(f"The result of subtracting is: {result}")

elif operation == "Multiply":
    result = num1 * num2
    print(f"The result for Multiplying is: {result}")

elif operation == "Divide":
    result = num1 / num2
    if num2 == 0:
        print("Error: Division by 0 is not allowed.")

else:
    print("Invalid operation, Please choose from ('Add', 'Subtract', 'Multiply', or 'Divide')")




    