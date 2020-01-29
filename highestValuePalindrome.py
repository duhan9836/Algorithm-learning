def hVP(s, n, k):
    l=[]
    diff=0
    for i in range(n):
        l.append(s[i])
    for i in range(n//2):
        if s[i]!=s[-1-i]:
            diff+=1
    if diff>k:
        return -1
    else:
        for i in range(n//2):
            if l[i]!=l[n-1-i] and diff<k:
                if l[i]=='9' or l[n-1-i]=='9':
                    diff-=1
                    k-=1
                else:
                    diff-=1
                    k-=2
                l[i],l[n-1-i]='9','9'
            elif l[i]!=l[n-1-i] and diff==k:
                maxi = max(int(l[i]),int(l[n-1-i]))
                l[i]=str(maxi)
                l[n-1-i]=str(maxi)
                diff-=1
                k-=1
    new_s="".join(l)
    return new_s

s='0011'
n=4
k=1

print(hVP(s,n,k))