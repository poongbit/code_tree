n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

# 상,하,좌,우
dx = [0,0,-1,1]
dy = [-1,1,0,0]

result = 0

for row in range(n):
    for column in range(n):
        # 인접한 개수 세기
        count = 0
        for i in range(4):
            new_row = row + dy[i]
            new_column = column + dx[i]

            if 0<=new_row<n and 0<=new_column<n:
                if grid[new_row][new_column] == 1:
                    count += 1

        
        if count >=3:
            result +=1

print(result)