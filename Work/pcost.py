# pcost.py
#
# Exercise 1.27
import sys


def portfolio_cost(filename):
    import csv
    portfolio_cost = 0.0
    with open(filename, 'rt') as f:
        csv_f = csv.reader(f)
        row = next(csv_f)
        for line in csv_f:
            try:
                name, shares, price = str(line[0]), int(line[1]), float(line[2])
            except ValueError:
                print('Error reading file ', filename)
            portfolio_cost += shares*price
    return(portfolio_cost)

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data\portfolio.csv'
cost = portfolio_cost(filename)
print(cost)