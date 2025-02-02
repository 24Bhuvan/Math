import numpy
import matplotlib.pyplot as plot
x=numpy.random.normal(5,1,100000)
plot.hist(x,100)
plot.show()