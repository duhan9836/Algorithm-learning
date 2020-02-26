def countingValleys(s):
    down=[]
    up=[]
    valley=0
    mountain=0
    for i in range(len(s)):
        if s[i]=='D':
            if len(up)!=0:
                up.pop()
            elif len(up)==0 and len(down)==0:
                valley+=1
                down.append('D')
            else:
                down.append('D')
        else:
            if len(down)!=0:
                down.pop()
            elif len(down)==0 and len(up)==0:
                mountain+=1
                up.append('U')
            else:
                up.append('U')
    return valley

s='DDDDUUDDUUUU'
print(countingValleys(s))