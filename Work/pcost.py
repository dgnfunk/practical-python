# pcost.py
#
# Exercise 1.27
import csv
import sys

def portfolio_cost(filename):
    'Getting the portfolio cost'
    total = 0
    if len(sys.argv) == 2:
        filename = sys.argv[1]

    with open(filename, 'rt') as file:
        rows = csv.reader(file)
        headers = next(rows)
        print(headers)

        for row in rows:
            # values = row.split(',')
            try:
                shares = int(row[1])
            except ValueError as err:
                print('Warrning! somthing missing.', err)

            price = float(row[2])
            totalPerShare = shares * price
            total = total + totalPerShare
            # print(values[0], totalPerShare)
    return total

cost = portfolio_cost('Data/portfolio.csv')
print('Total cost:', cost)