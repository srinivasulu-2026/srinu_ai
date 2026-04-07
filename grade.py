# 1. Take a score (0-100) as input
score = float(input("Enter your score: "))

# 2. Use multiple if statements for grade ranges
if score >= 90:
    print("Grade: A")
    print("Excellent work!")
elif score >= 80: # Python automatically handles the "and < 90" logic here
    print("Grade: B")
    print("Good job!")
elif score >= 70:
    print("Grade: C")
    print("Satisfactory")
elif score >= 60:
    print("Grade: D")
    print("Needs improvement")
else:
    print("Grade: F")
    print("Failed")

# 3. Additional specific checks
if score == 100:
    print("Perfect score!")

if score < 50:
    print("Please see instructor")