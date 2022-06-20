f=0
s=1
n=0

def fc_ser(f,s,n):
    if n==10:
        return 1
    else:
        print(f , end=" ")
        fc_ser(s,f+s,n+1)

fc_ser(f,s,n)

