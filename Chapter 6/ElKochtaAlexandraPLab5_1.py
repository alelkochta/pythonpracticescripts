################################################################# 
# Class: CMSC135
# Instructor: Shah, Madhvi
# Program Assignment: 5_1
# Program Name:      ElKochtaAlexandraPLab5_1.py
# Author:  El Kochta, Alexandra
# Due Date: 11/13/22
# Description: Give a brief description of each Program
# I pledge that I have completed the programming assignment independently.
# I have not copied the code from a student or any source.
# I have not given my code to any student.
# Print your Name here: Alexandra El Kochta
# Pseudocode: Write Pseudocode here for the program
# INITIALIZE SUM_OF to 0
# INITIALIZE TOTAL to 0
# OPEN numbers.txt for reading as file1
# FOR line IN file1
#   ADD 1 to total
#   ADD int(line) to sum_of
# CALULATE average as sum_of DIVIDED BY total
# DISPLAY average
###################################################################
sum_of = 0
total = 0
with open("numbers.txt", 'r') as file1:
    for line in file1:
        total += 1
        sum_of += int(line)
    average = sum_of / total
print(format(average, '.1f'))