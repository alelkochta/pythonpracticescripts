female_input = int(input("Enter the number of females: "))
male_input = int(input("Enter the number of males: "))
total_students = male_input + female_input
female_percentage = format((female_input / total_students), '.0%')
male_percentage = format((male_input / total_students), '.0%')
print("The class is", female_percentage, "female and", male_percentage, "male.")