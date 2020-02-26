def deciToOther(nums,base):
    ress = []
    residual = '0123456789ABCDEFGHIJKLMNOPQ'
    while nums > 0:
        res = f(nums%base)
        nums = nums//base
        ress.append(res)
    print(ress)
    n = len(ress)
    newnums = ''
    for i in range(n):
        num = ress.pop()
        newnums = newnums + str(num)
    return newnums

def f(num):
    residual = '0123456789ABCDEFGHIJKLMNOPQ'
    if num > 0 and num < len(residual):
        return residual[num]


print (deciToOther(1256,15))
print (deciToOther(1256,17))


