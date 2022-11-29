number_of_class_a = int(input("Enter count of A seats: "))
number_of_class_b = int(input("Enter count of B seats: "))
number_of_class_c = int(input("Enter count of C seats: "))
CLASS_A_PRICE = 20
CLASS_B_PRICE = 15
CLASS_C_PRICE = 10
def showIncome(a, b, c):
    class_a_total = a * CLASS_A_PRICE
    class_b_total = b * CLASS_B_PRICE
    class_c_total = c * CLASS_C_PRICE
    print("Income from class A seats: $", format(class_a_total, '.2f'), sep='')
    print("Income from class B seats: $", format(class_b_total, '.2f'), sep='')
    print("Income from class C seats: $", format(class_c_total, '.2f'), sep='')
    total_income = class_a_total + class_b_total + class_c_total
showIncome(number_of_class_a, number_of_class_b, number_of_class_c)
end = input("press enter to end program")
