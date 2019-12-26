def convertPost2(operateString):
    opening = '('
    closing = ')'
    operator_lst = ['+','-','*','/']
    operands = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    closings = []
    operates = []
    operators = []
    i = 0
    balanced = True
    while i < len(operateString) and balanced:
        symbol = operateString[len(operateString)-1-i]
        if symbol == closing:
            closings.append(symbol)
        if symbol in operator_lst:
            operators.append(symbol)
        if symbol in operands:
            operates.append(symbol)
        if symbol == opening:
            if closings == []:
                balanced = False
            else:
                closings.pop()
                operator = operators.pop()
                operates.append(operator)
        i+=1
    newstring=''
    for i in range(len(operates)):
        newstring = newstring + operates.pop()
    return newstring

operateString='((A+B)*(((C/D)+E)-F))'
print(convertPost2(operateString))
