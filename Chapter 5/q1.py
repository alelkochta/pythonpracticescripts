# Kilometer converter
def main1():
    km = float(input("Enter a distance in kilometers: "))
    convert(km)
def convert(kilometer):
    miles = kilometer * 0.6214
    print(kilometer, "kilometers is", format(miles, '.2f'), "miles")

main1()

def main():
    keep_going = 'y'
    while keep_going == 'y':
        km = float(input("Enter the distance in kilometers: "))
        convert(km)
        keep_going = input("Enter 'y' to keep going: ")

main()