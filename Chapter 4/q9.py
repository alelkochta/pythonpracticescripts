# Ocean Levels
ANNUAL_RISE = 1.6
total = 0.0
print("Year\n\nRise")
print("--------------------------")
for year in range(1, 27):
    total += ANNUAL_RISE
    print(year, "\t\t", format(total, '.1f'))

# ocean levels
# set an accumulator
yearly_increase=0

start_year=2019
end_year=2044

# print headings
print("Years\t\tOcean Rise in mm")
print("--------------------------------")

for y in range (start_year, end_year+1, 1):
    yearly_increase+=1.6
    print(y, "\t\t", format(yearly_increase, ".1f"))