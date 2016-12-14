# Copyright 2015 Enthought, Inc. All Rights Reserved
"""
Calculate Derivative
--------------------

Topics: NumPy array indexing and array math.

Use array slicing and math operations to calculate the
numerical derivative of ``sin`` from 0 to ``2*pi``.  There is no
need to use a 'for' loop for this.

Plot the resulting values and compare to ``cos``.

Bonus
~~~~~

Implement integration of the same function using Riemann sums or the
trapezoidal rule.

See :ref:`calc-derivative-solution`.
"""
import numpy
from matplotlib.pyplot import plot, show, subplot, legend, title

# calculate the sin() function on evenly spaced data.
x = numpy.array(numpy.linspace(0, 2 * numpy.pi, 101))
y = numpy.sin(x)

# calculate derivatives by slicing.
dx = x[1:] - x[:-1]
dy = y[1:] - y[:-1]
dy_dx = dy / dx

# calculate integral.
avg_height = (y[1:] + y[:-1]) / 2
integrals = dx * avg_height
integrals_summed = numpy.cumsum(integrals)

# plot sin x.
ax = subplot(2, 2, 1)
plot(x[:-1], y[:-1])
title("sin(x)")

# plot cos x.
subplot(2, 2, 2, sharex=ax, sharey=ax)
plot(x[:-1], numpy.cos(x[:-1]))
title("cos(x)")

# plot integral area.
subplot(2, 2, 3, sharex=ax, sharey=ax)
plot(x[:-1], integrals_summed)
title("accumulated integral of sin(x)")

# plot dy/dx.
subplot(2, 2, 4, sharex=ax, sharey=ax)
plot(x[:-1], dy_dx)
title("derivative of sin(x)")

show()
