numbers = [45, 23, 67, 89, 12, 56]

max_value = numbers[0]

position = 0

for i, num in enumerate(numbers):

  if num > max_value:

    max_value = num

    position = i

print(f"Maximum value: {max_value}")

print(f"Position: {position}")