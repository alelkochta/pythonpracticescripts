# Population
population = int(input("Starting number of organisms: "))
daily_increase = (int(input("Enter the average daily increase percentage: ")))
daily_increase_factor = (daily_increase / 100) + 1
days = int(input("Enter the number of days to multiply: "))
print("Day approximate\t\tPopulation")
for day in range(1, days+1):
    print(day, "\t\t\t", format(population, '.1f'))
    population = population * daily_increase_factor
