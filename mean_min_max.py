import numpy
import matplotlib.pyplot

# another very nice line

data = numpy.loadtxt(fname='data/inflammation-01.csv', delimiter=',')

# plot figures
fig = matplotlib.pyplot.figure(figsize=(10.0, 3.0))

# figure setup
axes1 = fig.add_subplot(1, 3, 1)
axes2 = fig.add_subplot(1, 3, 2)
axes3 = fig.add_subplot(1, 3, 3)

axes1.set_ylabel('average')
axes1.plot(numpy.mean(data, axis=0))

axes2.set_ylabel('max')
axes2.plot(numpy.max(data, axis=0))

axes3.set_ylabel('min')
axes3.plot(numpy.min(data, axis=0))

fig.tight_layout()

# show figure
matplotlib.pyplot.show()
