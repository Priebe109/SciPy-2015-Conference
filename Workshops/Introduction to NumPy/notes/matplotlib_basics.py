import numpy
import matplotlib.pyplot
from scipy.misc import face

# plotting multiple data sets.
x = numpy.arange(100) * 2 * numpy.pi / 100
matplotlib.pyplot.gcf().clear()
matplotlib.pyplot.plot(x, numpy.sin(x),
                       x, numpy.sin(2 * x))

# line formatting.
matplotlib.pyplot.gcf().clear()
matplotlib.pyplot.plot(x, numpy.sin(x), 'r-^')

# scatter plot.
x = numpy.linspace(0, 2 * numpy.pi, 50)
matplotlib.pyplot.gcf().clear()
matplotlib.pyplot.scatter(x, numpy.sin(x))

# color mapped scatter.
x = numpy.random.rand(200)
y = numpy.random.rand(200)
size = numpy.random.rand(200) * 30
color = numpy.random.rand(200)
matplotlib.pyplot.gcf().clear()
matplotlib.pyplot.scatter(x, y, size, color)
matplotlib.pyplot.colorbar()  # displays a color bar in the plot

# figure() creates a new figure (window) for all new plot()'s.
# subplot(rows, columns, active plot) creates a new subplot in the same figure for all new plot()'s.

# legends.
x = numpy.arange(100) * 2 * numpy.pi / 100
matplotlib.pyplot.gcf().clear()
matplotlib.pyplot.plot(numpy.sin(x), label='sin')
matplotlib.pyplot.plot(numpy.cos(x), label='cos')

matplotlib.pyplot.gcf().clear()
matplotlib.pyplot.plot(numpy.sin(x))
matplotlib.pyplot.plot(numpy.cos(x))
matplotlib.pyplot.legend(['sin', 'cos'])

# labels.
matplotlib.pyplot.xlabel('radians')
matplotlib.pyplot.ylabel('amplitude')

# close all figure windows with close('all').

# displaying images.
img = face(True)
matplotlib.pyplot.gcf().clear()
matplotlib.pyplot.imshow(img,
                         extent=[-25, 25, -25, 25],
                         cmap=matplotlib.pyplot.cm.get_cmap('bone'))
matplotlib.pyplot.colorbar()
matplotlib.pyplot.show()
