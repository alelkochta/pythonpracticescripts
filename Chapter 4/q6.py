# Celsius to Farenheit Table
print("Celsius\t\tFarenheit")
print("--------------------------")
for celsius in range(0, 21):
    farenheit = ((9/5) * celsius) + 32
    print(celsius, "\t\t", format(farenheit, '.1f'))

# celcius to fahrenheit table

# print headings
print("Celcius\t\tFahrenheit")
print("--------------------------")

# create loop structure
for c in range(0,21,1):
    fahrenheit=((9/5)*c)+32
    print(c,"\t\t", format(fahrenheit, ".2f"))