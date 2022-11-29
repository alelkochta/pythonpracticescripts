subtotal = 0.0
total_price = 0.0
SALES_TAX = 0.07
for item in range(5):
    price = float(input("Enter the price of the item "))
    subtotal += price
total = subtotal * (1 + 0.07)
print("The subtotal is $", format(subtotal, '.2f'), sep='')
print("The total is $", format(total, '.2f'), sep='')

    