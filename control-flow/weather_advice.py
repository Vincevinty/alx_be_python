#Ask for user input for weather conditions
weather = input("What's the weather like today? (sunny/rainy/cold): ")
# Provide advice based on the weather conditions
if weather.lower() == "sunny":
    print("Wear a t-shirt and sunglasses.")
elif weather.lower() == "rainy":
    print("Don't forget your umbrella and a raincoat.")
elif weather.lower() == "cold":
    print("Make sure to wear a warm coat and a scarf.")
else:
    print("I don't have advice for this weather condition.")
# End of the weather advice program
# This program provides weather-specific clothing advice based on user input
