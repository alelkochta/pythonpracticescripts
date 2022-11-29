# Nested Loops Pattern 1
number = 7
for i in range(number):
    for j in range(number - i):
        print("*", end='')
    print()

for i in range(7, 0, -1):
    for j in range(i):
        print("*", end='')
    print()

for r in range(8,1,-1):
    for c in range(r,1,-1):
        print("*", end='')      # using end to command that "Do not go to new line"
    print()
# Nested Loops Pattern 2
rows = 6
for r in range(rows):
    print("#", end='')
    for c in range(r):
        print(" ", end='')
    print("#")