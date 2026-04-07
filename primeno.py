def is_prime_number(num):
    # Prime numbers must be greater than 1
    if num <= 1:
        print(f"{num} is not a prime number")
        return

    # Check for divisors from 2 up to (but not including) the number
    for i in range(2, num):
        if num % i == 0:
            # If the remainder is 0, it's divisible by 'i' and not prime
            print(f"{num} is not a prime number")
            return
    
    # If the loop finishes without finding a divisor, it is prime
    print(f"{num} is a prime number")

# Taking user input
try:
    user_input = int(input("Enter a number: "))
    is_prime_number(user_input)
except ValueError:
    print("Please enter a valid integer.")