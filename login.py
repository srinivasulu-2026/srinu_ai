## Input data
username = input("Enter username: ")
password = input("Enter password: ")

# Level 1: Check if username is provided
if username != "":
    # Level 2: Check if password is provided
    if password != "":
        # Level 3: Check if username matches "admin"
        if username == "admin":
            # Level 4: Check if password matches "secret123"
            if password == "secret123":
                print("Login successful")
            else:
                print("Error: Incorrect password.")
        else:
            print("Error: Invalid username.")
    else:
        print("Error: Password not provided.")
else:
    print("Error: Username not provided.")