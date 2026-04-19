n, m = map(int, input().split())
arr = [[0] * m for _ in range(n)]

# Please write your code here.

# n*m을 벗어나지 않는 지 체크
def in_range(row,column):
    return 0<=row<n and 0<=column<m

# 달팽이 모양으로 이동, 90도 꺾어서 이동함
# 오,하,왼,위

d_row = [0,1,0,-1]
d_col = [1,0,-1,0]

# 시작은 오른쪽부터 이동
move_dir = 0

# 스타트 지점 기록
row,column = 0,0
arr[row][column] = 1

for i in range(2,n*m+1):
    n_row,n_col = row + d_row[move_dir], column + d_col[move_dir]

    if not in_range(n_row,n_col) or arr[n_row][n_col] !=0:
        # 90도 회전
        move_dir = (move_dir + 1) % 4

    # 검증된 후 실제 데이터에 반영
    row,column = row + d_row[move_dir], column + d_col[move_dir]

    # arr 배열에 반영
    arr[row][column] = i


for row in range(n):
    for column in range(m):
        print(arr[row][column],end = ' ')
    print()


