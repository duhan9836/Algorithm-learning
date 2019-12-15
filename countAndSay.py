def countAndSay(n):
    """
    :type n: int
    :rtype: str
    """
    if n==1:
        return '1'
    if n==2:
        return '11'
    if n>2:
        s=countAndSay(n-1)
        l=len(s)
        if l==2:
            if s[0]==s[1]:
                return ''.join([str(2),s[0]])
            else:
                return ''.join([str(1),s[0],str(1),s[1]])
        if l>2:
            s_=[]
            i=0
            while i<l-1:
                while s[i+1]==s[i] and i<l-1:
                    i+=1
                if s[i+1]:
                    s_.append(str(i))
                    s_.append(s[i])
                elif s[i]==s[i-1]:
                    s_.append(str(i))
                    s_.append(s[i])
                else:
                    s_.append(str(i-1))
                    s_.append(s[i-1])
                    s_.append(str(1))
                    s_.append(s[i])
            return ''.join(s_)

print(5,countAndSay(5))