#given a list of numbers, define a function to find the kth smallest item, with efficiency of O(nlog(n))
#simply sort the list and find the kth one,since the list sorting efficiency is O(nlog(n)), it already meets requirement.
import random

def findkth(alist,k):
    blist=sorted(alist)
    return blist[k-1]
n=10
k=5
list1=[random.randrange(100) for i in range(n)]
list2=[random.randrange(1000) for i in range(n)]
list3=[random.randrange(10000) for i in range(n)]

lists=[list1,list2,list3]

#for list in lists:
#   print(list,sorted(list),findkth(list,k))

#now try to find a more efficient way to solve the problem.
#to find the kth element, we don't have to fully sort the list, we just need to find the kth one
#remember when we implement the quick sort method, when fully applied the agorithm for each i, the pivot would just find its right place
#so for each sub list, if the right place for pivot is just the kth, we know the answer would be the pivot then.
#so we 分解 the question into smaller question, as to for each pivot, find its right place, and compare the place with k.

def findp(a,i,j):
    pivot=a[j]
    while i<j:
        if a[i]>pivot:
            a[j]=a[i]
            while j>i+1:
                j=j-1
                if a[j]<pivot:
                    a[i]=a[j]
                    a[j]=pivot
                    break
        i=i+1
    if a[i-1]>pivot:
        a[i-1]=pivot
        return i-1
    else:
        return j
b=[26, 42, 38, 33, 48, 58, 77, 76, 78, 98]

#print(findp(b,0,len(b)-1))
#print(b)

def find(a,k,i,j):
    p=findp(a,i,j)
    if p==k-1:
        return a[p]
    else:
        if p>k-1:
            j=p-1
        else:
            i=p+1
    return find(a,k,i,j)

def findk(a,k):
    return find(a,k,0,len(a)-1)
print(sorted(b))
print(findk(b,3))
