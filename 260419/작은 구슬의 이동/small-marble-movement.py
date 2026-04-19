n, t = map(int, input().split())
r, c, dir = input().split()
r, c = int(r), int(c)

# Please write your code here.


mapper = {
    'U' : 0,
    'L' : 1,
    'R' : 2,
    'D' : 3
}

row,column,move_dir = r-1,c-1,mapper[dir]

# 상,좌,우,하
dx = [0,-1,1,0]
dy = [-1,0,0,1]

# 범위 내에 들어갔는 지 확인

def in_range(row,column):
    return 0<= row < n and 0<=column<n


# 시뮬레이션 진행
for _ in range(t):
    n_row,n_column = row + dy[move_dir], column + dx[move_dir]

    if not in_range(n_row,n_column):
        move_dir = 3- move_dir

    else:
        row,column = n_row,n_column


print(row+1,column+1)