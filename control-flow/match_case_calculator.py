# match_case_calculator.py

# 1. Prompt for User Input
try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
except ValueError:
    print("Invalid input. Please enter valid numbers.")
    exit()

operation = input("Choose the operation (+, -, *, /): ")

# 2. Perform the Calculation Using Match Case:
result = None

match operation:
    case '+':
        result = num1 + num2
    case '-':
        result = num1 - num2
    case '*':
        result = num1 * num2
    case '/':
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
        else:
            result = num1 / num2
    case _:
        print("Invalid operation. Please choose from +, -, *, or /.")

# 3. Output the Result:
if result is not None:
    print(f"The result is {result}.")