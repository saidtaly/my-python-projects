import math
print("investment - to calculate the amount of interest you'll earn on your investment\nbond - to calculate the amount you'll have to pay on a home loan")
# Define function to calculate investment amount
def investment_amount():
    # Use try-except block to handle any potential errors in user input
    try:
        # Ask user for input
        deposit = float(input("Enter the amount of money that you are depositing: "))
        interest_rate = float(input("Enter the interest rate (as a percentage): "))
        years = int(input("Enter the number of years you plan on investing: "))
        interest = input("Do you want 'simple' or 'compound' interest? ")
        
        # Convert interest rate to decimal format
        interest_rate /= 100
        
        # Calculate investment amount
        if interest.lower() == "simple":
            investment = deposit * (1 + (interest_rate * years))
        elif interest.lower() == "compound":
            investment = deposit * math.pow((1 + interest_rate), years)
        else:
            print("Invalid input. Please enter 'simple' or 'compound'.")
            return
        
        # Print investment amount
        print(f"Your investment will be worth GBP{investment} after {years} years.")
    
    except:
        print("Invalid input. Please enter a valid number.")

# Define function to calculate bond repayment amount
def bond_repayment_amount():
    # Use try-except block to handle any potential errors in user input
    try:
        # Ask user for input
        present_value = float(input("Enter the present value of the house: "))
        interest_rate = float(input("Enter the interest rate (as a percentage): "))
        months = int(input("Enter the number of months you plan on taking to repay the bond: "))
        
        # Convert interest rate to decimal format
        interest_rate /= 12 * 100
        
        # Calculate bond repayment amount
        repayment = (interest_rate * present_value) / (1 - math.pow((1 + interest_rate), -months))
        
        # Print bond repayment amount
        print(f"Your monthly bond repayment will be GBP{repayment}.")
    
    except:
        print("Invalid input. Please enter a valid number.")

# Define main function to run program
def main():
    # Ask user for input
    choice = input("Enter either 'investment' or 'bond' from the menu above to proceed: ")
    
    # Determine which calculation to perform based on user input
    if choice.lower() == "investment":
        investment_amount()
    elif choice.lower() == "bond":
        bond_repayment_amount()
    else:
        print("Invalid input. Please enter 'investment' or 'bond'.")

# Call main function to run program
main()
