length_1 = float(input("enter the length of rectangle 1: "))
width_1 = float(input("enter the width of rectangle 1: "))
length_2 = float(input("enter the length of rectangle 2: "))
width_2 = float(input("enter the width of rectanble 2: "))
area_1 = format((length_1 * width_1), '.2f')
area_2 = format((length_2 * width_2), '.2f')
if area_1 == area_2:
    print("The rectangles have the same area!")
elif area_1 > area_2:
    print("Rectangle 1 has a greater area.")
else:
    print("Rectangle 2 has a greater area.")
    