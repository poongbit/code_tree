n, m = map(int, input().split())

# Please write your code here.

# 방문했던 공간 체크
visited = [[0]*m for _ in range(n)]

# 아래,오른쪽,위,왼쪽
d_row = [1,0,-1,0]
d_column = [0,1,0,-1]

def in_range(row,column):
    return 0<=row<n and 0<=column<m

# 원점 선언
row,column = 0,0

# 방문한 곳 체크
visited[row][column] = 1

# 이동 인덱스 선언
move_dir = 0

for i in range(2,n*m+1):
    n_row,n_column = row + d_row[move_dir], column + d_column[move_dir]

    if not in_range(n_row,n_column) or visited[n_row][n_column] !=0:
        # 방향 전환
        move_dir = (move_dir + 1) % 4

    
    row,column = row + d_row[move_dir], column + d_column[move_dir]

    visited[row][column] = i


for row in range(n):
    for column in range(m):
        print(visited[row][column],end=" ")
    print()
