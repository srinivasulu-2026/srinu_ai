def countdown():
    # Loop from 10 down to 1
    for i in range(10, 0, -1):
        # Print numbers on the same line with a space
        print(i, end=" ")
    
    # Move to a new line and print "Go!"
    print("\nGo!")

# Call the function to see the output
countdown()