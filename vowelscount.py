names = ["Alice", "Bob", "Emily", "David", "Oliver", "Sarah"]

vowels = ("A", "E", "I", "O", "U", "a", "e", "i", "o", "u")

count = 0

for name in names:

  if name.startswith(vowels):

    count += 1

print(f"Names starting with vowels: {count}")