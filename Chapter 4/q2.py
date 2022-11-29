# Calories Burned
print("Minutes\t\tCalories")
print("------------------------")
for i in range(10, 31, 5):
    burned = 4.2 * i
    print(i,"\t\t",burned)

# calories burned

cal_per_min=4.2

# print the headers
print("Minutes\t\tCalories")
print("------------------------")

for mins in range(10,31,5):
    calories=mins*cal_per_min
    print(mins,"\t\t",calories)