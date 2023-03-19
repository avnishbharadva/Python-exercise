import numpy

a = numpy.array([1,2,3,4])
b = a
b.shape = (2,2)  # it will also change shape of a bcz of copy (access same memory address)
print(a, id(a))
print(b, id(b))

a = numpy.array([[1,2,3],[4,5,6]])
b = a.view()  
a.shape = (3,2)  # it will not change shape of b
# b.shape = (3,2)  # it will not change shape of a
print(a, id(a))
print(b, id(b))

a = numpy.array([1,4,5,3])
b = numpy.copy(a)
# a.shape = (2,2)  # it will not change shape of b
b.shape = (2,2)  # it will not change shape of a
print(a, id(a))
print(b, id(b))