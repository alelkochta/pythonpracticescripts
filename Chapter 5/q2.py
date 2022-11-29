def main():
    global purchase_price
    purchase_price = float(input("Enter the purchase price in dollars: "))

    state_tax = s_tax(purchase_price)
    county_tax = c_tax(purchase_price)
    total_tax = t_tax(state_tax, county_tax)
    total_price = t_price(purchase_price, total_tax)

    display_output(purchase_price, state_tax, county_tax, total_tax, total_price)

def s_tax(price):
    S_TAX_AMOUNT = 0.05
    return price * S_TAX_AMOUNT

def c_tax(price):
    C_TAX_AMOUNT = 0.025
    return price * C_TAX_AMOUNT

def t_tax(state, county):
    return state + county

def display_output(price, state, county, total_tax, total_price):
    print("The price before tax is $", format(price, '.2f'), sep='')
    print("The state tax amount is $", format(state, '.2f'), sep='')
    print("The county tax amount is $", format(county, '.2f'), sep='')
    print("The total tax is $", format(total_tax, '.2f'), sep='')
    print("The total price is $", format(total_price, '.2f'), sep='')

def t_price(price, tax):
    return price + tax

main()
