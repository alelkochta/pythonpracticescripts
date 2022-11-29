# How much insurance?
def main():
    house_cost = float(input("Enter the replacement cost of the building: "))
    (insurance(house_cost))

def insurance(original_cost):
    INSURANCE_MULTIPLIER = .80
    insurace_price = original_cost * INSURANCE_MULTIPLIER
    print("The cost to insure this building is $", format(insurace_price, '.2f'), sep='')

main()