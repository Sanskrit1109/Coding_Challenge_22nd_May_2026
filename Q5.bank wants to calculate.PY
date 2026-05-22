#A bank wants to calculate simple interest for customers based on principal, rate, and time entered by the user.
#The formula for simple interest is: Simple Interest = (Principal * Rate * Time) / 100
#Get user input for principal, rate, and time
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest: "))
time = float(input("Enter the time in years: "))
#Calculate simple interest
simple_interest = (principal * rate * time) / 100
#Display the result
print(f"The simple interest is: {simple_interest}")

#Output:
#Enter the principal amount: 70
#Enter the rate of interest: 60
#Enter the time in years: 54
#The simple interest is: 2268.0