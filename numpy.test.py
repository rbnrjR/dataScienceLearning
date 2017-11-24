import numpy

numbers = [5,4,3,6,7]

# creating mean median and standard deviation for the numbers using numpy
mean = numpy.mean(numbers)
median = numpy.median(numbers)
std = numpy.std(numbers)

print('mean -- > ',mean)
print('median -- > ',median)
print('standard deviation -- > ',std)

# MATRIX -- >
a = [1,2]
b = [[2,4,6],[3,5,7]]

print(numpy.dot(a,b))

c = [[2,4,6],[3,5,7]]
d = [[2,6],[4,5],[6,3]]
print(numpy.dot(c,d))
