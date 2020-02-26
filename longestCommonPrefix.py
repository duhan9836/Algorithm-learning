def f(strs):
    if strs==[]:
        return ""
    else:
        n=min(map(len,strs))
        print(n)
        if n==0:
            return ""
        else:
            prefix=""
            i=0
            while len(set([a[i] for a in strs]))==1 and i<n:
                print([a[i] for a in strs])
                prefix=prefix+strs[0][i]
                i+=1
            return prefix



strs=["abcdeft","123456","yht"]
strs2=["abc","abcdefg","abdef"]
print(min(map(len,["a"])))
print(f(["a"]))