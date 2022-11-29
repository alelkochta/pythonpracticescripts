def main():
    num_emps = int(input("Enter the number of employee records you want to create: "))

    my_emp_file = open("Employee_Records.txt", 'w')

    for i in range(1, num_emps + 1):
        print("Employee #" + str(i))
        name = input("Name: ")
        id_num = input("ID Number: ")
        dept = input("Department: ")

        my_emp_file.write(name + '\n')
        my_emp_file.write(id_num + '\n')
        my_emp_file.write(dept + '\n')

        print()

    my_emp_file.close()
    print("Success!")

main()

def main1():
    emp_file = open('Employee_Records.txt', 'r')

    name = emp_file.readline()

    while name != '':
        id_num = emp_file.readline()
        dept = emp_file.readline()

        name = name.rstrip('\n')
        dept = dept.rstrip('\n')
        id_num = id_num.rstrip('\n')

        print("Name:", name)
        print("ID Number:", id_num)
        print("Department:", dept)

        print()

        name = emp_file.readline()

    emp_file.close()

main1()