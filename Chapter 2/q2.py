projected_sales = float(input("Enter the projected amount of total sales: "))
SALES_PERCENT = 0.23
profit = projected_sales * SALES_PERCENT
print("The profit amount for that amount of total sales is $", format(profit, '.2f'), sep='')
#hello