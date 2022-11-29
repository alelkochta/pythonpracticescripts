food_price = float(input("Enter the cost of the food: "))
TIP_PERCENT = .18
TAX_PERCENT = .07
tip_amount = food_price * TIP_PERCENT
tax_amount = food_price * TAX_PERCENT
total_fees = tip_amount + tax_amount
print("The tip amount is: $", format(tip_amount, '.2f'), ". The tax amount is: $", format(tax_amount, '.2f'), sep='')
print("The total price is: $", format((total_fees + food_price), '.2f'), sep='')

# Tip, Tax, and Total

# ask user to enter the charge for the food
price_def=float(input("Please enter the charge for the food: "))

tip=price_def*0.18
sales_tax=price_def*0.07

total=price_def+tip+sales_tax

# Display the data

print()
print("Your subtotal is", price_def)
print("Your tip amount is $", tip, sep='')
print("Your sales tax is $", format(sales_tax, ".2f"), sep='')
print()
print("Your total is $", total, sep='')