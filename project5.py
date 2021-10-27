RateOfGrowth = int(input("Please enter the rate of growth (in hours): "))
RogHours = int(input("Please enter the amount of hours it took to achieve "
                     "the rate of growth: "))
TotalHours = int(input("Please enter total hours of growth: "))
Organism = int(input("Please enter the starting number of organisms: "))

Hours = 0

while (Hours <= TotalHours):
    Organism *= RateOfGrowth
    Hours += RogHours
    if (Hours == TotalHours):
        break

print("The current total of the population is", Organism)
