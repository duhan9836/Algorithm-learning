board=[
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]


def isValidSudoku(board):
    rows=[]
    for row in board:
        row_=[row[i] for i in range(len(row)) if row[i]!="."]
        rows.append(row_)
    print(rows)

    columns=[]
    for j in range(len(board)):
        column=[row[j] for row in board if row[j]!="."]
        columns.append(column)
    print(columns)

    squares=[]
    row_inds=[[0,1,2],[3,4,5],[6,7,8]]
    column_inds=[[0,1,2],[3,4,5],[6,7,8]]
    square_indices=[]

    ss=[]
    for row_ind in row_inds:
        for column_ind in column_inds:
            s=[]
            for i in row_ind:
                for j in column_ind:
                    s.append((i,j))
            ss.append(s)

    for s in ss:
        square=[]
        for (i,j) in s:
            if board[i][j]!=".":
                square.append(board[i][j])
        squares.append(square)
    print(squares)

    check=rows+columns+squares

    for item in check:
        if len(set(item))!=len(item):
            return False
    return True

print(isValidSudoku(board))
