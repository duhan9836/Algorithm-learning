def findDiagonalOrder(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: List[int]
    """
    n = len(matrix)
    print ("length of matrix is", n)
    rows = {}
    cols = {}
    for i in range(n):
        if i % 2 == 1:
            rows[i] = [l for l in range(i + 1)]
            cols[i] = [l for l in range(i, -1, -1)]
        else:
            rows[i] = [l for l in range(i, -1, -1)]
            cols[i] = [l for l in range(i + 1)]
    for i in range(n, 2 * n-1):
        if i % 2 == 1:
            rows[i] = [l for l in range(i+1-n, n)]
            cols[i] = [l for l in range(n-1, i-n , -1)]
        else:
            rows[i] = [l for l in range(n-1, i-n , -1)]
            cols[i] = [l for l in range(i+1-n, n)]
    #print(rows)
    #print(cols)
    rows_ = []
    cols_ = []
    for i in range(2 * n-1):
        rows_ = rows_ + rows[i]
        cols_ = cols_ + cols[i]
    #print("length of rows_ is", len(rows_))

    inds = [(rows_[i], cols_[i]) for i in range(len(rows_))]
    result = [matrix[i][j] for (i, j) in inds]
    return result

matrix=[[i for i in range(j,j+3)] for j in range(1,8,3)]
print(matrix)
print(findDiagonalOrder(matrix))
