# Bug Collector
total = 0
for i in range(5):
    bugs_collected_today = int(input("Enter the number of bugs for today: "))
    total += bugs_collected_today
print(total)

bugs_total=0.0

# set repetition structure.
for day in range(5):     # it is five days.
    print("Enter the collected bugs for day", day+1, end='')
    bugs=int(input(": "))
    # add bugs to accumulator
    bugs_total+=bugs
# display the total bugs
print()
print("The total bugs collected: ", bugs_total)