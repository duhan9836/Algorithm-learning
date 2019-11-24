def find(a,b,n):
    low_a=0
    high_a=len(a)-1
    low_b=0
    high_b=len(b)-1
    while low_a<high_a and low_b<high_b:
        if a[low_a]+b[low_b]>n or a[high_a]+b[high_b]<n:
            return (-1,-1)
        elif a[low_a]+b[high_b]==n:
            return (low_a,high_b)
        elif a[low_a]+b[high_b]<n:
            low_a+=1
        else:
            high_b+=-1
    return (-1,-1)


l1=[1,2,3,4,5,6,7,8,9,10]
l2=[2,5,7,9,23,45,67,89,100]
n1=5
n2=19

L=[l1,l2]
N=[n1,n2]

for i in L:
    for j in L:
        for n in N:
            print ("{},{},{}, the result is {} ".format(i,j,n,find(i,j,n)))
