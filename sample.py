# x = [3, 4, -1, 1]
# x.sort()
# print(x)
# y = list(z for z in range(x[0], x[len(x)-1]))
# print(y)
# y = list(z for z in y if z not in x)
# print(y)
# if 0 in y: y.remove(0)
# print(y)
#


import numpy

a = [
    [ 5, 1, 9,11],
    [ 2, 4, 8,10],
    [13, 3, 6, 7],
    [15,14,12,16]
]


a = numpy.transpose(a)
print(a)
print(numpy.flip(a, 1))
print(numpy.flip(a, 0))

# import math

# print(round(pow(2.00000, 10), 8))

# x = [-2,1,-3,4,-1,2,1,-5,4]
# x.sort()
# print(x)