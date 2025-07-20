# multiplication_table.py

# 1. Prompt User for a Number:
try:
    number = int(input("Enter a number to see its multiplication table: "))
except ValueError:
    print("Invalid input. Please enter an integer.")
    exit()

# 2. Generate and Print the Multiplication Table:
print(f"Multiplication Table for {number}:")
for i in range(1, 11):  # Iterate from 1 to 10
    product = number * i
    print(f"{number} * {i} = {product}")