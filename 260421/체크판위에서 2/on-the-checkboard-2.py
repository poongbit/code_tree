R, C = map(int, input().split())
grid = [list(input().split()) for _ in range(R)]

# Please write your code here.

result = 0

# 시작 지점에서 출발함
for r1 in range(1,R):
    for c1 in range(1,C):
        # 색깔을 정하고
        color = grid[r1][c1]

        if color != grid[0][0]:

            # 지금 색 상황에서 다시 새롭게 탐색해서,
            # 다른 색이 나오면 카운트

            for r2 in range(r1+1,R-1):
                for c2 in range(c1+1,C-1):

                    new_color = grid[r2][c2]

                    if color != new_color:
                        result +=1

                

print(result)
                        
