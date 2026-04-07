# 1. Take a number as input from the user
# We use float() so the program can handle both integers and decimals
number = float(input("Enter a number: "))

# 2. Check if the number is positive
if number > 0:
    print("Positive number")

# 3. Check if the number is negative
elif number < 0:
    print("Negative number")

# 4. If it's neither positive nor negative, it must be zero
else:
    print("Zero")