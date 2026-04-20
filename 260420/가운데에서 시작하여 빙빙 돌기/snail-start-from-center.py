n = int(input())
grid = [[0] * n for _ in range(n)]

# Please write your code here.

# 역순으로 채워넣기 

visited = [[0] * n for _ in range(n)]

# 왼, 위, 오,아
d_row = [0,-1,0,1]
d_col = [-1,0,1,0]

# 맨 끝점 시작
row,column = n-1,n-1

visited[n-1][n-1] = n*n

start_index = 0

def in_range(row,column):
    return 0<=row<n and 0<=column<n

for i in range(n*n-1,0,-1):
    n_row,n_col = row + d_row[start_index], column + d_col[start_index]

    if not in_range(n_row,n_col) or visited[n_row][n_col] !=0:
        start_index = (start_index + 1) % 4

    row,column = row + d_row[start_index], column + d_col[start_index]

    visited[row][column] = i


for i in range(n):
    for j in range(n):
        print(visited[i][j], end = " ")
    
    print()