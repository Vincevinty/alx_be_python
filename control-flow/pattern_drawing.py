# This script is part of a pattern drawing module.
# Prompt user to enter positive integer that represents the size of the pattern.
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
current_row = 0

# While loop to draw the pattern
while current_row < size:
    

# For loop for columns in the current row
    for current_column in range(size):
        print("*", end="")
    print()  # Move to the next line after printing all columns in the current row
    current_row += 1  # Increment the row counter


