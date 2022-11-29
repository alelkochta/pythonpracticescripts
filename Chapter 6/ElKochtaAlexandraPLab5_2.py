
################################################################# 
# Class: CMSC135
# Instructor: Shah, Madhvi
# Program Assignment: 5_2
# Program Name:      ElKochtaAlexandraPLab5_2.py
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
# TRY OPEN numbers.txt for reading as file1
# FOR line IN file1
#   ADD 1 to total
#   ADD int(line) to sum_of
# CALULATE average as sum_of DIVIDED BY total
# IF IOError occurs, DISPLAY error message
# IF ValueError occurs, DISPLAY error message
# IF no error occurs, DISPLAY average
###################################################################
sum_of = 0
total = 0
try:
    with open("numbers.txt", 'r') as file1:
        for line in file1:
            total += 1
            sum_of += int(line)
        average = sum_of / total
except IOError:
    print("An error occured while trying to read the file.")
except ValueError:
    print("Non-numeric data found in the file.")
else:
    print(format(average, '.1f'))

