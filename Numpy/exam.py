import numpy

# a = numpy.array([1,2,3])

# print(a)
# print(type(a))
# print(type(a[0]))

# b = numpy.array([[1,2,3],[4,5,6]])
# print(b)

# c = numpy.array([1,2,3,4,5], ndmin=2)
# print(c)

# d = numpy.array([1,2,3,4], dtype=complex)
# print(d)

# a = numpy.array([[1,2,3],[4,5,6]])
# print(a)
# print(a.shape)
# a.shape = (3,2)
# print(a,a.shape)
# b = a.reshape(3,2)
# print(b)

# a = numpy.array([[1,2,3,4],[5,6,7,8]])
# print(a.ndim)

# a = numpy.arange(10)
# print(a)
# print(type(a))

# a = numpy.array([1,2,3,4], dtype=numpy.int8)
# print(a.itemsize)
# b = numpy.array([1,2], dtype=numpy.int16)
# print(b.itemsize)
# a = numpy.array([1,2,3,4], dtype=numpy.int32)
# print(a.itemsize)
# b = numpy.array([1,2], dtype=numpy.int64)
# print(b.itemsize)

# a = numpy.empty([2,2])  
# print(a)    # it will store garbage value

# a = numpy.zeros([3,2])
# c = numpy.zeros((4,2))
# print(c)
# print(a)
# b = numpy.ones([3,3])
# print(b)

# a = [1,2,3]
# x = numpy.asarray(a)
# print(x,type(x))
# b = [(1,2),(3,4)]
# c = numpy.asarray(b)
# print(c)

# a = b'Hello world'
# # print(a, type(a))
# c = numpy.frombuffer(a, dtype='S1')
# print(c.itemsize)
# print(type(c[0]))

# a = numpy.arange(10)
# print(a)
# b = numpy.arange(1,10,2)
# print(b)

# a = numpy.linspace(1,10,2)
# print(a)
# b = numpy.linspace(1,9,3,endpoint=True)
# print(b)

# a = numpy.logspace(1,10,num=10,base=8)
# print(a)

# a = numpy.arange(11)
# b = a[slice(2,7,2)]
# print(b)
# print(a[9])
# print(a[1:8:2])
# print(a[:])
# print(a[8:])
# print(a[:4])

# a = numpy.array([[1,2,3],[4,5,6],[7,8,9]])
# print(a[1:])
# print(a[...,1:])
# print(a[:2])
# print(a[1])

# a = numpy.array([[1,2,3],[4,5,6]])
# b = a[[0,1,1],[0,1,0]]
# print(b, type(b))

# x = numpy.array([[ 0, 1, 2],[ 3, 4, 5],[ 6, 7, 8],[ 9, 10, 11]])
# rows = numpy.array([[0,0],[3,3]])
# cols = numpy.array([[0,2],[0,2]])
# y = x[rows,cols] 
# print(y)

# a = numpy.array([[1,2,3],[5,2,7],[3,2,6],[4,2,7]])
# print(a[a!=2])

# a = numpy.array([[1,2,3,4],[5,6,7,8]])
# b = numpy.array([10,20,30,40])
# c = a * a
# c = a * b
# b = numpy.array([10,20,30,40])
# c = a + b
# print(c)

# a = numpy.array([[1,2],[3,4],[5,6]])
# for i in numpy.nditer(a):
#     print(i)

# a = numpy.array([[1,2],[3,4],[5,6]])
# b = a.T
# print(b)

# a = numpy.arange(0,60,5) 
# b = a.reshape(3,4)
# print(b)
# c = b.copy(order = 'C')
# print(c)
# d = b.copy(order = 'F')
# print(d)

# a = numpy.array([[1,2],[6,4]])
# for i in numpy.nditer(a,op_flags=['readwrite']):
#     i[...] = 2*i

# print(a)

# a = numpy.array([1,2])
# a[1] = 4
# for i in range(2):
#     a[i] = a[i]*a[i]
# print(a)

# a = numpy.array([[1,2,3],[4,5,6],[7,8,9]])
# b = numpy.array([11,22,33])
# for x,y in numpy.nditer([a,b]):
#     print(x,y)

# a=numpy.array([15],dtype=numpy.uint8)
# a = 4
# print(bin(a))
# print(numpy.bitwise_and(a,b))
# print(numpy.bitwise_or(a,b))
# print(numpy.bitwise_not(a))
# print(numpy.left_shift(a,2))
# print(numpy.right_shift(a,2))
# print(numpy.binary_repr(a))

print(numpy.char.add(["avnish"],["bharadva"]))