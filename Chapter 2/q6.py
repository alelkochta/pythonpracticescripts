STATE_TAX = .05
COUNTY_TAX = 0.025
purchase_amount = float(input("Enter the purchase amount: "))
state_tax = purchase_amount * STATE_TAX
county_tax = purchase_amount * COUNTY_TAX
total_tax = county_tax + state_tax
print("The state tax is:", format(state_tax, '.2f'))
print("The county tax is:", format(county_tax, '.2f'))
print("The total tax is:", format(total_tax, '.2f'))
total_amount = purchase_amount + total_tax
print("The total price is $", format(total_amount, '.2f'), sep='')

purchase=float(input("Enter the amount of purchase: "))

# Calculate state and county sales tax
state_tax=purchase*0.05
county_tax=purchase*0.025
total_tax=state_tax+county_tax

# Display the results.

print()
print("Your purchase amount is $", purchase, sep='')
print("Your state tax is $", format(state_tax, ".2f"), sep='')
print("Your county tax is $", format(county_tax, ".2f"), sep='')
print("Your total tax is $", total_tax, sep='')
print()
print("Your total is $", purchase+total_tax, sep='')