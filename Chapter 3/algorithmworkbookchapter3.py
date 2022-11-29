# 1
x = int(input())
if x > 100:
    y = 20
    z = 40
print(y, z)
# 2
a = int(input())
if a < 10:
    b = 0
    c = 1
print(b,c)
# 3
a = int(input())
if a < 10:
    b = 0
else:
    b = 99
print(b)
# 5
amount1 = int(input("1: "))
amount2 = int(input("2: "))
if (amount1 > 10) and (amount2 < 100):
    if (amount1 > amount2):
        print(amount1)
    else:
        print(amount2)
# 6
speed = int(input("Speed: "))
if (speed >= 24) and (speed <= 56):
    print("Speed is normal")
else:
    print("Speed is abnormal")
# 7
point = int(input("point variable: "))
if (point <= 9) or (point >= 51):
    print("invalid points")
else:
    print("valid points")