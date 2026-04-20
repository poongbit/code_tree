N, T = map(int, input().split())
str = input()
board = [list(map(int, input().split())) for _ in range(N)]

# Please write your code here.

# 시계 방향

d_row = [0,1,0,-1]
d_col = [1,0,-1,0]

start_index = 3

row,col = N // 2,  N//2 

def in_range(row,col):
    return 0<=row<N and 0<=col<N

# 스타트 지점의 점수 먹기
result = board[row][col]

for i in range(T):
    dir = str[i]

    if dir == 'L':
        start_index = (start_index -1 + 4) % 4

    elif dir == 'R':
        start_index = (start_index + 1) % 4

    else:
        n_row,n_col = row + d_row[start_index], col + d_col[start_index]

        if in_range(n_row,n_col):
            result += board[n_row][n_col]
            # 이동
            row,col = n_row,n_col

        else:
            continue

print(result)

