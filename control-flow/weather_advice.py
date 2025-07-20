#Ask for user input for weather conditions
weather = input("What's the weather like today? (sunny/rainy/cold): ")
# Provide advice based on the weather conditions
if weather.lower() == "sunny":
#sunny: Wear a t-shirt and sunglasses.
    print("Wear a t-shirt and sunglasses.")
elif weather.lower() == "rainy":
#rainy: Don't forget your umbrella and a raincoat.
    print("Don't forget your umbrella and a raincoat.")
elif weather.lower() == "cold":
#cold: Make sure to wear a warm coat and a scarf.
    print("Make sure to wear a warm coat and a scarf.")
else:
    print("I don't have advice for this weather condition.")
# End of the weather advice program

