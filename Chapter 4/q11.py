# Weight Loss
start_weight = int(input("Enter your starting weight in whole pounds: "))
end_weight = start_weight
print("Month\t\tWeight")
POUNDS_PER_MONTH = 4
for i in range(1,7):
    end_weight -= POUNDS_PER_MONTH
    print(i, "\t\t", end_weight)