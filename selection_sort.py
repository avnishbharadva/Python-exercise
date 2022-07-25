lst = [-56,23,97,-4,11,90,-45,103,0,5]

for i in range(0,len(lst)):
    for j in range(i+1,len(lst)):
        if lst[i]>lst[j]:
            lst[i],lst[j] = lst[j],lst[i]
        
print(lst)