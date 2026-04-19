n, m = map(int, input().split())
arr = [[0] * m for _ in range(n)]

# Please write your code here.

def in_range(row,column):
    return 0<=row<n and 0<=column<m

# 달팽이 모양식 이동
# 오,아,왼,위
d_row = [0,1,0,-1]
d_col = [1,0,-1,0]

row,column = 0,0 # 시작은 0,0
dir_num = 0

# 처음 시작 위치에 초기값을 적는다
arr[row][column] = 1

# n*n번 진행한다.
for i in range(2,n*m + 1):
    # 현재 방향 dir를 기준으로 그 다음 위치값을 계산한다.

    n_row,n_col = row + d_row[dir_num], column + d_col[dir_num]

    # 더이상 나갈 수 없다면
    # 시계 방향으로 90 도 회전한다. 

    if not in_range(n_row,n_col) or arr[n_row][n_col] !=0:
        dir_num = (dir_num + 1) % 4

    # 그 다음 위치로 이동한 배열에 올바른 값을 넣어줌
    
    row,column = row + d_row[dir_num], column + d_col[dir_num]
    arr[row][column] = i


# 출력

for row in range(n):
    for column in range(m):
        print(arr[row][column], end = ' ')

    print()