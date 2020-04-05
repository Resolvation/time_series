import csv
from matplotlib import pyplot as plt
import numpy as np


def get_data(name: str, column='Last'):
    """Returns column from name.csv.
    
    The csv file for this function should be taken from
    https://www.nasdaq.com/market-activity/stocks/*/historical, where '*' is the name of company.
    """
    number = {'Last': 1, 'Open': 3, 'High': 4, 'Low': 5}[column]
    
    with open(name+'.csv', 'r') as csvfile:
        data_reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        res = np.array([float(e[2:]) for e in [row[number] for row in data_reader][:0:-1]])
    
    return res


def plot_prices(data, name=''):
    plt.plot(data)
    plt.title(name)
    plt.xlabel('days')
    plt.ylabel('price, $')
    plt.xlim(0, len(data))
    plt.ylim(0, 1.1 * max(data))
    plt.grid()
    plt.show()
