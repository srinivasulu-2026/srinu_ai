# 1. Takes user's age as input
# We use int() to convert the text input into a number
age = int(input("Enter your age: "))

# 2. If age is 18 or above, print "You can vote"
if age >= 18:
    print("You can vote")

# 3. If age is 21 or above, print "You can drink alcohol (in US)"
if age >= 21:
    print("You can drink alcohol (in US)")

# 4. Always print "Thank you" at the end
print("Thank you")