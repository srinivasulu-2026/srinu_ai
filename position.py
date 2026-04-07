numbers = [5, 2, 8, 2, 9, 2, 1, 2]

target = 2

indices = []

for i, val in enumerate(numbers):

  if val == target:

    indices.append(i)

print(f"Value {target} found at positions: {indices}")