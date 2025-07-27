# A function that performs basic arithmetic operations
def perform_operation(num1, num2, operation):
    """
    Executes arithmetic operations.

    Args:
        num1 (float): The first number for the operation.
        num2 (float): The second number for the operation.
        operation (str): Accepts 'add', 'subtract', 'multiply', or 'divide'.

    Returns:
        float or str: The result or error message.
    """
    operation = operation.lower()

    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num2 == 0:
            return "Error: Division by 0 is not allowed."
        return num1 / num2
    else:
        return "Invalid operation. Choose 'add', 'subtract', 'multiply', or 'divide'."

#  Call the function with user input
if __name__ == "__main__":
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    operation = input("Choose operation: ") 

    result = perform_operation(num1, num2, operation)
    print(f"Result: {result}")