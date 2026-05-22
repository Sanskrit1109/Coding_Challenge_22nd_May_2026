#A grocery shop owner wants to calculate the final bill after applying discounts based on the purchase amount. Write a program using if...elif...else to display the final amount.
print("Enter the purchase amount :")
amount = float(input())
if amount > 500:
    discount = 0
elif amount <= 500 and amount > 1000:
    discount = 0.5/100 * amount
elif amount <= 1000 and amount > 5000:
    discount = 1.0/100 * amount
else : discount = 1.5/100 * amount
final_amount  = amount - (amount  * discount / 100)

print("The final amount after discount is : ", final_amount)
