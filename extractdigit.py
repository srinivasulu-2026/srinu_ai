# Input: A 3-digit number
number = int(input("inter a three digit number: "))

# Extracting digits using provided hints
ones = number % 10
tens = (number // 10) % 10
hundreds = number // 100

# Output format
print(f"Hundreds: {hundreds}, Tens: {tens}, Ones: {ones}")