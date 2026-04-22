n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

max_count = 0

for row in range(n):
    for column in range(n-2):

        for n_row in range(n):
            
            # 같은 행에 속하는 경우
            if row == n_row:
                for n_col in range(column+3,n-2):

                    max_count = max(max_count, arr[row][column] + arr[row][column+1] + arr[row][column+2]
                    + arr[n_row][n_col] + arr[n_row][n_col+1] + arr[n_row][n_col+2])

            else:
                # 전 열 탐색 가능
                for n_col in range(n-2):
                    max_count = max(max_count, arr[row][column] + arr[row][column+1] + arr[row][column+2]
                    + arr[n_row][n_col] + arr[n_row][n_col+1] + arr[n_row][n_col+2])


print(max_count)
                    
        