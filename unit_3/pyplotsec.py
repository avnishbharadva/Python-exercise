from matplotlib import pyplot as plt 
import numpy 

x = numpy.array([3,5,6])
y = 2 * x + 5

plt.plot(x,y,marker='v',markersize=15,label="Line 1")
plt.plot([2,7,1],[9,4,2],marker='v',markersize=15,label="Line 2")
plt.legend()
# plt.plot(x,y)
# marker types :
# o
# 
# plt.scatter(x,y)
plt.show()