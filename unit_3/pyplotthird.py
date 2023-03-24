from matplotlib import pyplot as plt

plt.figure(1)
# tick_label = ['one','two','three','four']
# plt.plot([1,2,3,4],[5,6,7,8],marker="s",markersize=20)
# plt.bar([1,2,3,4],[5,6,7,8],tick_label=tick_label)
# plt.pie([3,7,8,6],labels=['three','seven','eight','six'],explode=[1.0,0,0,0],shadow=True,radius=1.1,startangle=90)
# plt.scatter([3,2,1,6],[6,7,3,2],label="ndwfi")
# plt.bar([1,2],[4,5])
# plt.subplot(132)
# plt.hist([3,5,6,7,1],[4,8,2,9],histtype='bar')

population_age = [21,21,22,23,25,27,30,42,40,1,2,102,95,8,15,105,70,65,55,70,75,60,52,25,25,21,45]  
bins = [0,10,20,30,40,50,60,70,80,90,100]  
plt.hist(population_age, bins, histtype='bar', rwidth=0.8)

# plt.legend()
# plt.xlim(1,3)
# plt.ylim(5,7)

# Marker
# 1,2,3,4
# +,P
# o,.
# ^,v,<,>
# h,H
# |,_
# x,s
# d,D
# *
plt.show()