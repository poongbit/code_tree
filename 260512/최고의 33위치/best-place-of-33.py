n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.


max_score = 0

for row in range(0,n-2):
    for column in range(0,n-2):
        score = 0

        # 내부 순화

        for dr in range(3):
            for dc in range(3):
                score += grid[row+dr][column+dc]


        

        max_score = max(max_score,score)
    

print(max_score)