n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

max_coin = 0

for row in range(n):
    for column in range(n-2):
        coin = grid[row][column] + grid[row][column+1] + grid[row][column+2]

        max_coin = max(max_coin, coin)

print(max_coin)
