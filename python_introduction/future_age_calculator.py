
# Assign values to variables.
while True:
    try:
        current_age = int(input("How old are you? "))
        break
    except ValueError:
        print("Please enter a valid integer for your age.")
future_years = 2050
current_year = 2023
# Calculating future age.
future_age = current_age + (future_years - current_year)
# Print the result.
print(f"In {future_years}, you will be {future_age} years old.")