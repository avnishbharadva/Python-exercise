import numpy as nmp
arr = nmp.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# print(arr[slice(1, 5, 2)])

arr1 = arr[3]
# print(arr1)

arr2 = arr[3:6:2]
# print(arr2)

arr3 = arr[3:]
# print(arr3)

arr4 = arr[:6]
# print(arr4)

arr5 = arr[::2]
# print(arr5)

arr6 = arr[:6:2]
# print(arr6)

arr7 = arr[-3:-1]
# print(arr7)

arr8 = arr[-3:]
# print(arr8)

# arr9 = nmp.array([[1,2,3],[4,5,6],[7,8,9]])
# print(arr9)
# print(arr9[0,1])
# print(arr9[0:2,1:3]) # first two rows and second and third columns
# print(arr9[0:2]) # first two rows
# print(arr9[...]) # all rows
# print(arr9[0,...]) # first row
# print(arr9[...,1]) # second column
# print(arr9[0,...,1]) # first row and second column
# print(arr9[...,1:]) # second column and all rows

# print(arr9[(1,2,0),(0,2,1)])

# print(arr9[arr9<=5])

# ar = nmp.array([10,20,30,40])
# br = nmp.array([1,2,3,4])
# cr = ar + br
# print(cr)

# ar = nmp.array([10,20,30,40])
# br = nmp.array([2])
# cr = ar + br
# print(cr)

# ar = nmp.array([[10,20],[30,40]])
# br = nmp.array([1,2])
# cr = ar + br
# print(cr)

# ar = nmp.array([[10,20],[30,40]])
# br = nmp.array([5])
# cr = ar + br
# print(cr)

# ar = nmp.array([[10,20],[30,40]])
# for i in nmp.nditer(ar):
#     print(i)

# ar = nmp.array([10,20,30,40])
# for i in nmp.nditer(ar):
#     print(i)

# ar = nmp.array([[10,20],[30,40]])
# am = ar.T # transpose
# print(am)

# ar = nmp.array([[10,20],[30,40]])
# am = ar.copy() # copy
# print(am)

# ar = nmp.array([[10,20],[30,40]])
# am = ar.view() # view
# print(am)

# ar = nmp.array([[10,20],[30,40]])
# for i in nmp.nditer(ar, op_flags=['readwrite']):
#     i[...] = i*i
# print(ar)

ar = nmp.array([[10,20],[30,40]])
ar2 = nmp.array([50,60])
ar3 = ar + ar2
for x,y in nmp.nditer([ar,ar2]):
    print(x,y)
print(ar3)