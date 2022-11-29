file = open('test.txt', 'w')
for num in range(1, 11):
    file.write(str(num) + '\n')
file.close()

file1 = open('data.txt', 'r')
line1 = file1.readline()
while line1 != '':
    line1 = line1.rstrip('\n')
    print(line1)
    line1 = file1.readline()

file1.close()

file1 = open('data.txt', 'r')

for line in file1:
    line = line.rstrip('\n')
    print(line)

file1.close()