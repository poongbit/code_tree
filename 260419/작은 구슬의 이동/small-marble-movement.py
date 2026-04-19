n, t = map(int, input().split())
r, c, dir = input().split()
r, c = int(r), int(c)

# Please write your code here.

# 0-based index에 어룰리게 변경
row,column = r-1,c-1

# (0번 3번)과 (1번 2번)이 서로 반대가 되도록 설계

# 상,좌,우,하

dx = [0,-1,1,0]
dy = [-1,0,0,1]

mapping = {
    'U' : 0,
    'L' : 1,
    'R' : 2,
    'D' : 3
}

# 초기 방향 채택
move_dir = mapping[dir]

# 좌표 안에 들어갔는 지 확인
def in_range(row,column):
    return 0<=row<n and 0<=column<n

# 시뮬레이션 진행
for _ in range(t):
    n_row,n_column = row + dy[move_dir], column + dx[move_dir]

    if in_range(n_row,n_column):
        # 그대로 바꿔줌
        row,column = n_row,n_column

    else:
        # 방향을 90도로 바꿈
        move_dir = 3 - move_dir

print(row+1,column+1)