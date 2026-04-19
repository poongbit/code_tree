n, m = map(int, input().split())
points = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.

color = [[0]*m for _ in range(n)]

# 위,아래,왼,오
d_row = [-1,1,0,0]
d_col = [0,0,-1,1]


for r,c in points:
    # 0-based index로 변환
    row,column = r-1,c-1

    # 1로 색칠 표기
    color[row][column] = 1

    # 막 색칠한 상태에서 4방향 탐색후 카운트 계산
    count = 0

    for i in range(4):
        n_row = row + d_row[i]
        n_col = column + d_col[i]

        if 0<=n_row<n and 0<=n_col<m:
            if color[n_row][n_col] == 1:
                count +=1
    

    if count ==3:
        print(1)

    else:
        print(0)
