SUGAR_RATIO = (1.5 / 48)
BUTTER_RATIO = (1 / 48)
FLOUR_RATIO = (2.75 / 48)

user_cookies = int(input("How many cookies do you want to make? "))
sugar_amount = format((user_cookies * SUGAR_RATIO), '.2f')
butter_amount = format((user_cookies * BUTTER_RATIO), '.2f')
flour_amount = format((user_cookies * FLOUR_RATIO), '.2f')

print("To make", user_cookies, "cookies, you need:")
print(sugar_amount, "cups of sugar,", butter_amount, "cups of butter, and", flour_amount, "cups of flour.")