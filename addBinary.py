def addBinary(a,b):
    #suppose len(a)>=len(b)
    #1. convert a,b into list, from end to beginning
    #note the data type, the difference between string adding and int adding
    aa=[int(a[len(a)-1-i]) for i in range(len(a))]
    bb=[int(b[len(b)-1-i]) for i in range(len(b))]+[0]*(len(a)-len(b))
    #2. define an assistant viariable cc, for 进位
    cc=[0]*len(a)
    for i in range(1,len(a)):
        if aa[i-1]+bb[i-1]+cc[i-1]>1:
            cc[i]=1
        else:
            cc[i]=0
    #3. calculate the sum
    dd=[0]*len(a)
    for i in range(len(a)):
        if aa[i]+bb[i]+cc[i] in (0,2):
            dd[i]=0
        if aa[i]+bb[i]+cc[i] in (1,3):
            dd[i]=1
    if aa[len(a)-1]+bb[len(a)-1]+cc[len(a)-1]>1:
        dd.append(1)
    #4.convert dd back to string:
    dd_=''
    for i in range(len(dd)):
        dd_=dd_+str(dd[len(dd)-1-i])
    return dd_
a=["1111","1011011","11100011"]
b=["11","10","101","110"]
for i in a:
    for j in b:
        print((i,j),addBinary(i,j))

