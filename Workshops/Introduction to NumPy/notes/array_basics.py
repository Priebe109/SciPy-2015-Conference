import numpy
import matplotlib.pyplot

# arrays can be created with lists, tuples etc.
a = numpy.array([1, 2, 3, 4, 5])
b = numpy.array((2, 3, 4, 5, 6))
print("a = " + str(a))
print("b = " + str(b))

# arrays of the same dimensions can be added (element-wise).
c = a + b
print("a + b = " + str(c))

# a scalar can be broadcast to an array by addition.
d = a + 10
print("a + 1 = " + str(d))

# numpy array ranges can be created with the arange method.
e = numpy.arange(21)
print("e = " + str(e))

# standard operations with scalars are broadcast element-wise.
f = e * 2 * numpy.pi / 21

# the type of a numpy array is numpy.ndarray.
print(type(f))
print(f.dtype)
print(f.itemsize)
print(f.shape)
print(f.size)  # number of elements.
print(f.ndim)  # number of dimensions.

# array indexing.
a = numpy.array([1, 2, 3, 4, 5])
print(a[0])

# filling an array.
a.fill(0)
print(a)

# alternately (slower).
a[:] = 1
print(a)

# slicing var[lower:upper:step] -> [lower, upper).
a = numpy.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(a[1:3])

# negative indices work also.
print(a[1:-2])
print(a[-4:-2])

# omitting indices.
print(a[:3])
print(a[-2:])

# step.
print(a[::2])  # even
print(a[1::2])  # odd
