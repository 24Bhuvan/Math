import numpy
import matplotlib
import matplotlib.pyplot as plot
x=numpy.random.uniform(0,5,10000)
plot.hist(x,5)
plot.show()