# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    """Converts Fahrenheit to Celsius using the global conversion factor."""
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """Converts Celsius to Fahrenheit using the global conversion factor."""
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    unit = input("Enter the temperature unit (C for Celsius, F for Fahrenheit): ").strip().upper()
    temp_str = input("Enter the temperature value: ").strip()

    try:
        temp = float(temp_str)
    except ValueError:
        raise ValueError("Invalid temperature. Please enter a numeric value.")

    if unit == 'F':
        celsius = convert_to_celsius(temp)
        print(f"{temp}°F is {celsius:.2f}°C")
    elif unit == 'C':
        fahrenheit = convert_to_fahrenheit(temp)
        print(f"{temp}°C is {fahrenheit:.2f}°F")
    else:
        raise ValueError("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

if __name__ == "__main__":
    main()