miles_driven = float(input("Enter the number of miles driven: "))
gallons_of_gas_used = float(input("Enter the number of gallons of gas used: "))
miles_per_gallon = miles_driven / gallons_of_gas_used
print("You averaged", format(miles_per_gallon, '.2f'), "miles per gallon.")