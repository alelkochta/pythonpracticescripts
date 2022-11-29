# 9
number = int(input("Please enter a number between 0 and 100: "))
while (number < 1) or (number > 100):
    print("This number is invalid")
    number = int(input("Please enter a valid number: "))
# 8 
number = int(input("Enter a positive non-zero number: "))
while (number <= 0):
    print("This number is invalid.")
    number = int(input("Enter a valid number, please: "))
print(number)
# 7
rows = 10
columns = 15
for i in range(rows):
    for j in range(columns):
        print("#", end='')
    print()
# 1
product = 0
while (product < 100):
    user_input = int(input("Enter a number: "))
    product = user_input * 10
print(product)
# 2 
again = "y"
while again == "y":
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    sum = num1 + num2
    print(sum)
    again = input("Enter 'y' to go again or 'n' to quit: ")
# 3
for i in range(0, 1001, 10):
    print(i)
# 4
total = 0
for i in range(10):
    user_number = int(input("Enter a number: "))
    total += user_number
print(total)
# 5
total = 0.0
for i in range (1, 31):
    total += (i/(31-i))