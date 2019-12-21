def spiral(matrix):
    m,n=len(matrix),len(matrix[0])
    i_start=0
    i_end=m-1
    j_start=0
    j_end=n-1
    ind=spiralIndex(i_start,j_start,i_end,j_end)
    res=[]
    for r in ind:
        res.append(matrix[r[0]][r[1]])
    return res

def spiralIndex(i_start,j_start,i_end,j_end):
    if i_start>i_end or j_start>j_end:
        return []
    elif i_end==i_start:
        return [(i_start,j) for j in range(j_start,j_end+1)]
    elif j_end==j_start:
        return [(i,j_start) for i in range(i_start,i_end+1)]
    else:
        s1=[(i_start,j) for j in range(j_start,j_end+1)]
        s2=[(i,j_end) for i in range(i_start+1,i_end+1)]
        s3=[(i_end,j) for j in range(j_end-1,j_start-1,-1)]
        s4=[(i,j_start) for i in range(i_end-1,i_start,-1)]
        return s1+s2+s3+s4+spiralIndex(i_start+1,j_start+1,i_end-1,j_end-1)

print(spiralIndex(0,0,3,3))
matrix=[]
for i in range(5):
    matrix.append([j+i+4 for j in range(4)])

print(matrix)
print(spiral(matrix))
