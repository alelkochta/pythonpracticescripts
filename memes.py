def main():
    my_list = []
    for i in range(1, 11):
        print("Enter number", i, "of 10: ", end ='')
        number = float(input())
        my_list.append(number)
    print(my_list)
    #min_and_max(my_list)
    print("The total is:", total(my_list))
    #average(my_list)

#def min_and_max(list):

def total(list):
    total = 0
    for i in list:
        total += i
    return(total)

#def average(list):




if __name__ == "__main__":
    main()