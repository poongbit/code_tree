n, m = map(int, input().split())

# Please write your code here.

# 기록할 공간
visited = [[0]*m for _ in range(n)]

# 방향 : 오,아래,왼,위

d_row = [0,1,0,-1]
d_col = [1,0,-1,0]

# 원점 위치 설정
row,column = 0,0

visited[row][column] = 'A'

start_index = 0


alpha = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N',
'O','P','Q','R','S','T','U','V','W','X','Y','Z']

def in_range(row,column):
    return 0<=row<n and 0<=column<m


for i in range(2,n*m+1):
    n_row,n_col = row + d_row[start_index] , column + d_col[start_index]

    if not in_range(n_row,n_col) or visited[n_row][n_col] != 0:
        start_index = (start_index + 1) % 4

    row,column = row + d_row[start_index] , column + d_col[start_index]

    alpha_index = (i-1) % 26

    visited[row][column] = alpha[alpha_index]


for i in range(n):
    for j in range(m):
        print(visited[i][j], end = " ")

    print()
    