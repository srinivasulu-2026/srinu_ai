# Inputs
bill_amount = 85.00
tip_rate = 0.18  # 18% expressed as a decimal
people = int(input("enter number of persons: "))

# 1. Calculate tip amount
tip_amount = bill_amount * tip_rate

# 2. Calculate total
total_bill = bill_amount + tip_amount

# 3. Split among 4 people
amount_per_person = total_bill / people

# Displaying the results
print(f"--- Tip Calculator Results ---")
print(f"Bill Amount:      ${bill_amount:.2f}")
print(f"Tip Amount (18%): ${tip_amount:.2f}")
print(f"Total Bill:       ${total_bill:.2f}")
print(f"Split (4 people): ${amount_per_person:.2f} per person")