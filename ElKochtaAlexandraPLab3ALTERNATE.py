################################################################# 
# Class: CMSC135
# Instructor: Shah, Madhvi
# Program Assignment: 3
# Program Name: ElKochtaAlexandraPLab3ALTERNATE.py
# Author: Alexandra El Kochta
# Due Date: 10/09/22
# Description: Give a brief description of each Program
# I pledge that I have completed the programming assignment independently.
# I have not copied the code from a student or any source.
# I have not given my code to any student.
# Print your Name here: Alexandra El Kochta
# Pseudocode: Write Pseudocode here for the program
# Prompt user for number of years
# INITIALIZE total to 0.0
# INITIALIZE average to 0.0
# FOR years in RANGE (1, user_years + 1)
#   DISPLAY "For year:" number_of_years
#   FOR month in range (1,13)
#       prompt user for the rainfall amounf for each month
#       total = total + this_month_rainfall
# average = total / (user_years * 12)
# DISPLAY the total number of months
# DISPLAY the total rainfall amount
# DISPLAY the average rainfall amount
###################################################################

user_years = int(input("How many years do you want to calculate for: "))
total = 0.0
average = 0.0
for years in range(1, user_years + 1): # outer loop once per year
    print("For year:", (years))
    for month in range(1, 13): # inner loop once per month
        this_month_rainfall = float(input("Enter the rainfall amount for this month: "))
        total += this_month_rainfall
average = total / (user_years * 12)
print("For", (user_years * 12), "months:")
print("The total rainfall is:", format(total, '.2f'), "inches.")
print("The average monthly rainfall is:", format(average, '.2f'), "inches. ")       