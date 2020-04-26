from pandas import read_csv
from matplotlib import pyplot

series = read_csv('./input/daily-total-female-births-CA.csv', header=0, index_col=0)
pyplot.plot(series)
pyplot.show()
pyplot.savefig('./output/female-daily-births.png')