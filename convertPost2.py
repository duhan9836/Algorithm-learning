def convertPost2(operateString):
    opening = '('
    closing = ')'
    operator_lst = ['+','-','*','/']
    operands = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    openings = []
    operates = []
    operators = []
    i = 0
    balanced = True
    while i < len(operateString) and balanced:
        symbol = operateString[i]
        if symbol == opening:
            openings.append(symbol)
        if symbol in operator_lst:
            operators.append(symbol)
        if symbol in operands:
            operates.append(symbol)
        if symbol == closing:
            if openings == []:
                balanced = False
            else:
                openings.pop()
                operator = operators.pop()
                operates.append(operator)
        i+=1
    return "".join(operates)

operateString='((A+B)*(((C/D)+E)-F))'
print(convertPost2(operateString))
