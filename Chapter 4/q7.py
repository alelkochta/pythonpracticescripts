number_of_days = int(input("Enter the number of days: "))
print("Day\t\tPay")
print("---------------------")
total_pay = 0
day_pay = 0.01
for day in range(1, (number_of_days + 1)):
    print(day, "\t\t $", day_pay, sep='')
    total_pay += day_pay
    day_pay *= 2
total_pay_in_dollars = total_pay
print("The total pay is $", total_pay_in_dollars)

days=int(input("Enter the number of days to calculate: "))

# print headings
print()
print("Days\tSalary in $")
print("-----------------------------")

# set an accumulator and create loop structure
salary=0.01 # the first day is one penny
total=0
for d in range(1,days+1,1):
    print(d,"\t$", salary)
    total += salary
    salary*=2
    
# show total   
print() 
print("The total earnings is ${}".format(total, ",.2f"))