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



def yanghui2(n):
    if n == 1:
        return [[1]]
    if n == 2:
        return [[1], [1, 1]]
    if n>2:
        y = [1]*n
        for i in range(1, n-1):
            y[i]=yanghui2(n-1)[-1][i-1]+yanghui2(n-1)[-1][i]
        print(y)
        return yanghui2(n-1).append(y)
    
    

def yanghui3(n):
    yanghui=[[1]*(i+1) for i in range(n)]
    for i in range(2,n):
        for j in range(1,i):
            yanghui[i][j]=yanghui[i-1][j-1]+yanghui[i-1][j]
    return yanghui

print(yanghui3(10))

