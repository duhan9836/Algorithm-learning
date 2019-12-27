def convertPost3(operateString):
    operateList = [i for i in operateString if i!=" "]
    print(operateList)
    prec = {}
    prec['*'] = 3
    prec['/'] = 3
    prec['+'] = 2
    prec['-'] = 2
    prec['('] = 1
    ops = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    postfixList=[]
    temptList=[]
    for symbol in operateList:
        if symbol == "(":
            temptList.append(symbol)
        elif symbol in ops:
            postfixList.append(symbol)
        elif symbol == ")":
            tempt = temptList.pop()
            while tempt != "(":
                postfixList.append(tempt)
        else:
            while len(temptList)>0 and prec[temptList[-1]] > prec[symbol]:
                postfixList.append(temptList.pop())
            temptList.append(symbol)
    while len(temptList)>0:
        postfixList.append(temptList.pop())
    return "".join(postfixList)

operate1 = ' A + B  *  C + D '
operate2 = " A + B  * C"
operate3 = "A + B * C"
operate4 = "A * B + C * D"
operate5 = " A + B  * C -  D - E  *  F + G "
operates = [operate1,operate2,operate3,operate4,operate5]

for operate in operates:
    print(operate,":",convertPost3(operate))