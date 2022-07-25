lst = [-9,0,-34,12,7,48,9,21]

for i in range(len(lst)-1):
    for j in range(len(lst)-i-1): #last value set after one iteration so that we write len - i - 1
        if lst[j]>lst[j+1]:
            lst[j],lst[j+1] = lst[j+1],lst[j]

print(lst)