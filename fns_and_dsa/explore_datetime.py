# explore_datetime.py

from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print("Current Date and Time:", formatted_date)

def calculate_future_date():
    try:
         days_to_add = int(input("Enter the number of days to add to the current date: "))

         future_date = datetime.now() + timedelta(days=days_to_add)
         print("Future Date:", future_date.strftime("%Y-%m-%d"))
    except ValueError:
        print("Please enter a valid integer for the number of days.")

# Run both functions
if __name__ == "__main__":
    display_current_datetime()
    calculate_future_date()