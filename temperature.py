def celsius_to_fahrenheit():
    # Ask the user to enter the temperature in Celsius
    celsius = float(input("Enter temperature in Celsius: "))
    
    # Apply the formula: F = (C * 9/5) + 32
    fahrenheit = (celsius * 9/5) + 32
    
    # Print the result formatted to one decimal place as shown in the example
    print(f"{celsius}°C is equal to {fahrenheit:.1f}°F")

# Call the function
celsius_to_fahrenheit()