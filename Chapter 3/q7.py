color1 = (input("Enter a primary color: ")).lower()
color2 = (input("Enter another primary color: ")).lower()
if ((color1 == "red") and (color2 == "blue")) or ((color1 == "blue") and (color2 == "red")):
    print("purple")
elif ((color1 == "red") and (color2 == "yellow")) or ((color1 == "yellow") and (color2 == "red")):
    print("orange")
elif ((color1 == "blue") and (color2 == "yellow")) or ((color1 == "yellow") and (color2 == "blue")):
    print("green")
else:
    print("invalid primary colors.")