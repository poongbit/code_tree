n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

max_cnt = 0

for row in range(n):
    for col in range(n-2):
        for n_row in range(n):

            # 두 격자가 같은 행에 있는 경우
            if row == n_row:
                for n_col in range(col+3,n-2):

                    max_cnt = max(max_cnt,arr[row][col]+arr[row][col+1]+arr[row][col+2]
                    + arr[n_row][n_col] + arr[n_row][n_col+1] + arr[n_row][n_col+2])

            else:
                for n_col in range(n-2):
                    max_cnt = max(max_cnt,arr[row][col]+arr[row][col+1]+arr[row][col+2]
                    + arr[n_row][n_col] + arr[n_row][n_col+1] + arr[n_row][n_col+2])


    
print(max_cnt)
                
        