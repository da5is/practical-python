# pcost.py
#
# Exercise 1.27

def portfolio_cost(filename):
    portfolio_cost = 0.0
    with open(filename, 'rt') as f:
        row = next(f)
        for line in f:
            row = line.split(',')
            name, shares, price = str(row[0]), int(row[1]), float(row[2])
            portfolio_cost += shares*price
    return(portfolio_cost)

cost = portfolio_cost('Data\portfolio.csv')
cost = portfolio_cost('Data\missing.csv')
print(cost)