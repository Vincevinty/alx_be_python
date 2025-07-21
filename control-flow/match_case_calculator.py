#A script to prompt the user to enter two numbers and select an operation (+, -, *, /)
# Prompt user to enter two numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number; "))

# Prompt user to select an operation
operation = input("Choose the operation (+, -, *, /): ")

# Match case to perform the selected operation
match operation:
    
    case "+":
        result = num1 + num2
        print(f"The result is {result}")
    
    case "-":
        result = num1 - num2
        print(f"The result of is {result}")
    
    case "*":
        result = num1 * num2
        print(f"The result is {result}")

    case "/":
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
        
        else:
            result = num1 / num2
            print(f"The result is {result}")

    case _:
        print("Invalid operation selected. Please choose from (+, -, *, or /).")

# End Program

    
