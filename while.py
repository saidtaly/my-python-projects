# Initialize an empty list to store the input numbers
list = []

# Loop indefinitely until the user enters -1 to stop
while True:
    try:
        # Prompt the user to enter a number and convert the input to a float
        number = float(input("Please enter a number: "))
        
        # Check if the user entered -1 to stop; if so, break out of the loop
        if number == -1:
            break
        else:
            # Add the valid input number to the list
            list.append(number)
    
    # If the input cannot be converted to a float, catch the ValueError exception
    except ValueError:
        print("Invalid input! Please enter only a number.")

# Compute the average of the numbers in the list and print the result
average = sum(list) / len(list)
print("The average is:", average)
