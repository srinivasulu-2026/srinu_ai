# 1. Take age as input and convert to integer
age = int(input("Enter age: "))

# 2. Take student status as input (expecting 'yes' or 'no')
student_input = input("Are you a student? (yes/no): ").lower()
is_student = (student_input == "yes")

# Hint: Outer if checks age
if age < 18:
    # Inner if checks student status for children
    if is_student:
        price = 5 # Child student: $5
    else:
        price = 7 # Child non-student: $7
else:
    # Inner if checks student status for adults
    if is_student:
        price = 8 # Adult student: $8
    else:
        price = 10 # Adult non-student: $10

# Display the result
print(f"Ticket price: ${price}")