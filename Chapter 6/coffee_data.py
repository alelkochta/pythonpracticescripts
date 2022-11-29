def main():
    another = 'y'

    c_file = open('coffee_file.txt', 'a')

    while (another == 'y') or (another == 'Y'):
        
        print("Enter the following data for the coffee record: ")
        descr = input("Enter the description of the coffee: ")
        qty = int(input("Enter the quantity of this coffee type: "))

        c_file.write(descr + '\n')
        c_file.write(str(qty) + '\n')

        print("Do you want to add another record? Press 'y' to add another.")
        another = input()

    c_file.close()
    print("Data successfully appended to the file.")

main()

def read():
    c_file = open('coffee_file.txt', 'r')

    descr = c_file.readline()

    while descr != '':
        qty = c_file.readline()

        descr = descr.rstrip('\n')
        qty = qty.rstrip('\n')
        
        print("Description:", descr)
        print("Quantity:", qty)
        print()

        descr = c_file.readline()
    c_file.close()

read()