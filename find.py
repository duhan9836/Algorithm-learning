def find(a,b,n):
    low_a=0
    low_b=0
    high_a=len(a)-1
    high_b=len(b)-1

    while low_a<=high_a and low_b<=high_b:
        if a[low_a]+b[low_b]>n or a[high_a]+b[high_b]<n:
            return (-1,-1)
        elif a[low_a]+b[high_b]==n:
            return (low_a,high_b)
        elif a[low_a]+b[high_b]<n:
            lower_a=low_a
            upper_a=high_a
            while lower_a<=upper_a:
                mid_a=(lower_a+upper_a)//2
                if a[mid_a]+b[high_b]==n:
                    return (mid_a,high_b)
                elif a[mid_a]+b[high_b]<n:
                    lower_a=mid_a+1
                else:
                    upper_a=mid_a-1
            low_a=lower_a

        else:
            lower_b=low_b
            upper_b=high_b
            while lower_b<=upper_b:
                mid_b=(lower_b+upper_b)//2
                if a[low_a]+b[mid_b]==n:
                    return (low_a,mid_b)
                elif a[low_a]+b[mid_b]<n:
                    lower_b=mid_b+1
                else:
                    upper_b=mid_b-1
            high_b=upper_b

l1=[1,2,3,4,5,6,7,8,9,10]
l2=[3,4,6,8,34,67,89]


n1=5
n2=100

L=[l1,l2]
N=[n1,n2]

#test
for i in L:
    for j in L:
        for n in N:
            print ("for {} {} {}, result is {}".format(i,j,n,find(i,j,n))) 
