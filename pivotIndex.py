def pivotIndex(a):
    if len(a)==1:
        return 0
    if len(a)>1:
        if sum(a[1:]) == 0:
            return 0
        elif sum(a[:len(a)]) == 0:
            return len(a) - 1
        elif len(a) == 2:
            return -1
        else:
            for i in range(1,len(a)-1):
                if sum(a[(i + 1):]) == sum(a[:i]):
                    return i
                else:
                    return -1

num1=[9,8,7,6,5,4,3,2,1,0,1,2,3,4,5,6,7,8,9]
num2=[0,1]
num3=[1,0]

print(pivotIndex(num1))

print(sum(num1[:9]))
print(sum(num1[10:]))

nums=[num1,num2,num3]
for num in nums:
    print(pivotIndex(num))