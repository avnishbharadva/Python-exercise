arr = [23,56,7,3,98,67,45]
arr.sort()

def binary_search(arr,low,high,f):

    if low<=high:
        mid = (low+high)//2
        if arr[mid]==f:
            return mid
        else:
            if arr[mid]<f:
                return binary_search(arr,mid+1,high,f)
            else:
                return binary_search(arr,low,mid-1,f)


print(arr)
fv = int(input("Enter Value For Find : ")) 

length = len(arr)-1
print(fv,"is placed on",binary_search(arr,0,length,fv),"index")