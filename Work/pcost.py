# pcost.py
#
# Exercise 1.27
total_cost = 0.0

with open('Data\portfolio.csv', 'rt') as f:
    line = next(f)
    for line in f:
        split_line = line.split(",")
        name = str(split_line[0])
        shares = int(split_line[1])
        price = float(split_line[2])
        total_cost += shares * price

print(total_cost)