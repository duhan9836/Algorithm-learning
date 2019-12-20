def findDiagonalOrder(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: List[int]
    """
    #the number of diagonals: m+n-1
    #the sum of index for items on kth diagonals: i+j=k
    #the number of items for the kth diagonals:
    #if m==n: for k in range(m), number is k+1
    #         for k in range(m,m+n-1), number is m-(k-(m-1))=2m-k-1
    #if m!=n: for k in range(minmn), number is k+1
    #         for k in range(minmn,maxmn), number is minmn
    #         for k in range(maxmn,m+n-1), number is minmn+maxmn-k-1
    #start/end index:
    #for k%2==1: i starts from max(0,k-n+1)
    #for k%2==0: j starts from max(0,k-m+1)

    m = len(matrix)
    n = len(matrix[0])
    num_of_diag=m+n-1
    minmn=min(m,n)
    maxmn=max(m,n)
    index_list=[]
    if m==n:
        for k in range(m):
            start_i=max(0,k-n+1)
            start_j=max(0,k-m+1)
            l=k+1
            if k%2==1:
                index_list=index_list+[(i,k-i) for i in range(start_i,start_i+l)]
            else:
                index_list=index_list+[(k-j,j) for j in range(start_j,start_j+l)]
        for k in range(m,num_of_diag):
            start_i = max(0, k - n + 1)
            start_j = max(0, k - m + 1)
            l = 2*m-k-1
            if k%2==1:
                index_list=index_list+[(i,k-i) for i in range(start_i,start_i+l)]
            else:
                index_list=index_list+[(k-j,j) for j in range(start_j,start_j+l)]
    else:
        minmn = min(m, n)
        maxmn = max(m, n)
        for k in range(minmn):
            start_i=max(0,k-n+1)
            start_j=max(0,k-m+1)
            l=k+1
            if k%2==1:
                index_list=index_list+[(i,k-i) for i in range(start_i,start_i+l)]
            else:
                index_list=index_list+[(k-j,j) for j in range(start_j,start_j+l)]
        for k in range(minmn,maxmn):
            start_i=max(0,k-n+1)
            start_j=max(0,k-m+1)
            l=minmn
            if k%2==1:
                index_list=index_list+[(i,k-i) for i in range(start_i,start_i+l)]
            else:
                index_list=index_list+[(k-j,j) for j in range(start_j,start_j+l)]
        for k in range(maxmn,num_of_diag):
            start_i = max(0, k - n + 1)
            start_j = max(0, k - m + 1)
            l = minmn+maxmn-k-1
            if k%2==1:
                index_list=index_list+[(i,k-i) for i in range(start_i,start_i+l)]
            else:
                index_list=index_list+[(k-j,j) for j in range(start_j,start_j+l)]
    print(index_list)
    matrix_list=[]
    for (i,j) in index_list:
        matrix_list.append(matrix[i][j])
    return matrix_list


def find2(matrix):
    ret = []
    m, n = len(matrix), len(matrix[0])
    for s in range(m+n-1):
        if s%2==1:
            seq=range(0,s+1)
        else:
            seq=range(s,-1,-1)
        for i in seq:
            if i < m  and s-i < n:
                ret.append(matrix[i][s-i])
    return ret

matrix=[[i for i in range(j,j+4)] for j in range(1,13,4)]
print(matrix)
#print(findDiagonalOrder(matrix))
print(find2(matrix))