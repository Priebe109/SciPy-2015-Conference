import numpy

# multi-dimensional arrays are created as a sequence of sequences.
a = numpy.array([[0, 1, 2, 3],
                 [10, 11, 12, 13]])

print('shape = ' + str(a.shape))
print('dimensions = ' + str(a.ndim))

# access index by tuples: a[row, column].
print(a[0, 1])
print(a[1, 0])

# access row.
print(a[1])

# slicing.
b = numpy.arange(30)
b.shape = 5, 6
print(b)
print(b[0, 3:5])
print(b[4:, 4:])
print(b[:, 2])
print(b[2::2, ::2])

# simple smoothing filter
upper = b[:-2, 1:-1]
center = b[1:-1, 1:-1]
b[1:-1, 1:-1] = (center + upper) / 2
print(b)
