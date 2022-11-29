mass = float(input("Enter the object's weight in kilograms: "))
weight = mass * 9.8
if weight < 100:
    print("The object is too light.")
elif weight > 500:
    print("The object is too heavy.")
else: 
    print("The object weighs", format(weight, '.2f'), "newtons")