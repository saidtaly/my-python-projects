# Read in the times for swimming, cycling, and running
swim_time = int(input("Enter the time for swimming (in minutes): "))
cycle_time = int(input("Enter the time for cycling (in minutes): "))
run_time = int(input("Enter the time for running (in minutes): "))

# Calculate the total time taken to complete the triathlon
total_time = swim_time + cycle_time + run_time

# Check the total time against the qualifying time and display the appropriate award
if total_time <= 100:
    print("Congratulations! You have earned Provincial Colours.")
elif total_time <= 105:
    print("Congratulations! You have earned Provincial Half Colours.")
elif total_time <= 110:
    print("Congratulations! You have qualified for a Provincial Scroll award.")
else:
    print("Sorry, you did not qualify for an award.")
