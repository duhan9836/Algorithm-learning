def yanghui(n):
    res=[]
    for i in range(1,n+1):
        res.append(row(i))
    return res

def row(n):
    if n==1:
        return [1]
    if n==2:
        return [1,1]
    if n>2:
        y=[1]*n
        for i in range(1,n-1):
            y[i]=row(n-1)[i-1]+row(n-1)[i]
        return y
print(row(10))
print(yanghui(10))