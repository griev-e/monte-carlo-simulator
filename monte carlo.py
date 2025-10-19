import random

# asks user for starting price
print()
startprice = input("Stock Price: ")

# asks user how many days to simulate
print()
days = input("Days to Simulate: ")

# asks user positive return percentage per day
print()
positivereturn = input("Positive Percent Change per Day: ")

# asks user negative return percentage per day
print()
negativereturn = input("Negative Percent Change per Day: ")

# asks user how many simulations
print()
simulations = input("Simulation Count: ")

# convert inputs to numbers
price = float(startprice)
numdays = int(days)
numsims = int(simulations)
posreturn = float(positivereturn) / 100
negreturn = -float(negativereturn) / 100

finalprices = []
for sim in range(numsims):
    price = float(startprice)
# loops through number of days chosen
    for day in range(numdays):
        daily = random.uniform(negreturn,posreturn)
        price = price * (1 + daily)
    finalprices.append(price)

# After the loops, analyze results
print()
print(" - Results - ")
print()
print(f"Starting Price: ${round(float(startprice), 2)}")
print(f"Average Final Price: ${round(sum(finalprices) / len(finalprices), 2)}")
print(f"Best Case: ${round(max(finalprices), 2)}")
print(f"Worst Case: ${round(min(finalprices), 2)}")
print()