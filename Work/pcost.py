# pcost.py
#
# Exercise 1.27
total_cost = 0.0

with open('Data\portfolio.csv', 'rt') as f:
    line = next(f)
    for line in f:
        print(line)
        name = str(line[0])
        shares = int(line[1])
        price = float(line[2])
        total_cost += shares * price

print(total_cost)