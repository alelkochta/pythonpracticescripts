def main():
    found = False

    search = input("Enter a seach term: ")
    
    c_file = open("coffee_file.txt", 'r')

    descr = c_file.readline()

    while descr != '':
        qty = float(c_file.readline())

        descr = descr.rstrip('\n')

        if descr == search:
            print("Description:", descr)
            print("Quantity:", qty)
            print()
            found = True

        descr = c_file.readline()
        
    c_file.close()
    if not found:
        print("That search returned no results.")

main()