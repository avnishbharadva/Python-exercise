import matplotlib.pyplot as plt
# import pylab as plt    # pylab = numpy + pyplot
import numpy

# x_axis = numpy.array([3,8])
y_axis = numpy.array([1,10])

plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.title("my first graph")
# plt.plot(x_axis, y_axis)
# plt.plot(x_axis,y_axis, marker='o')
# plt.plot(x_axis,y_axis,marker='*')
# plt.plot(x_axis,y_axis,marker='o',color='green',linestyle='-.',mfc='blue',markersize=20)
plt.plot(y_axis,marker='o', ms=10, color='red',mec='blue')
# plot parameters :
# x_axis
# y-axis
# marker = 'o' or + , * , . , P , x , X
# color = 'green'    - marker line color
# mfc = 'blue'   - marker color
# markersize = 20
# linestyle = '--' or - , : , -. 
plt.show()