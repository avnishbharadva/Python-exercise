import numpy 

a = numpy.array([2,5,3,1])
print(numpy.sort(a))

a = numpy.array(['shivam','krupesh','avnish'])
print(numpy.sort(a))

a = numpy.array([[1,7,5],[4,7,2]])
print(numpy.sort(a))

a = numpy.array([[4,2],[6,3]])
print(numpy.sort(a,axis=1))

a = numpy.array([1,4,6,2])
x = numpy.where(a==2)
print(x)

a = numpy.array([1,2,4,6,2,2])
x = numpy.where(a==2)
print(x)

a = numpy.array([1,6,4,7,9,12])
print(numpy.where(a%2==0))

a = numpy.array([23,4,5,6,7,4,6])
print(numpy.searchsorted(a,23))  # Find indices where elements should be inserted to maintain order

a = numpy.array([1,2,3,5])
print(numpy.searchsorted(a,1,side='right'))

a = numpy.array([5,6,7])
print(numpy.searchsorted(a,[1,2,3]))