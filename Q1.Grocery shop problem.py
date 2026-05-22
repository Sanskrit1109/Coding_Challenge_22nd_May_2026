#A grocery shop owner wants to calculate the final bill after applying discounts based on the purchase amount. Write a program using if...elif...else to display the final amount.

amount = float(input("Enter purchase amount: "))

if amount >= 5000:
    discount = amount * 0.20  
elif amount >= 3000:
    discount = amount * 0.15   
elif amount >= 1000:
    discount = amount * 0.10  
else:
    discount = 0               

final_amount = amount - discount

print("Discount:", discount)
print("Final Bill Amount:", final_amount)

#Enter purchase amount: 7500
#Discount: 1500.0
#Final Bill Amount: 6000.0