import numpy

# arr = numpy.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])

# print(numpy.average(arr))

# print(numpy.average(arr,axis=1))

# print(numpy.median(arr))

a = numpy.array([80,190,0])
print(numpy.percentile(a,50))
print(numpy.mean(a))
print(numpy.average(a))
print(numpy.median(a))
print(numpy.ptp(a))  # return max - min range