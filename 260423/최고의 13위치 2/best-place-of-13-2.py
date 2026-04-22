n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

max_cnt = 0

for row in range(n-1):
    for col in range(n-2):

        for n_row in range(row+1,n):
            for n_col in range(n-2):

                max_cnt = max(max_cnt,arr[row][col]+arr[row][col+1]+arr[row][col+2]
                + arr[n_row][n_col] + arr[n_row][n_col+1] + arr[n_row][n_col+2])

    
print(max_cnt)
                
        