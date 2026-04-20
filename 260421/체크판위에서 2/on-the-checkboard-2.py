R, C = map(int, input().split())
grid = [list(input().split()) for _ in range(R)]

# Please write your code here.

result = 0

# 시작 지점에서 출발함
for r1 in range(1,R):
    for c1 in range(1,C):
        for r2 in range(r1+1,R-1):
            for c2 in range(c1+1,C-1):

                # 전부 다른 경우에만 개수를 센다
                if grid[0][0] != grid[r1][c1] and \
                    grid[r1][c1] != grid[r2][c2] and \
                    grid[r2][c2] != grid[R-1][C-1]:
                        result +=1 
                

print(result)
                        
