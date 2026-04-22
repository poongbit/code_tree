n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

# 격자를 놓는다.
max_cnt = 0

for row in range(n):
    # 격자를 벗어나지 않을 범위로만 잡는다.
    for column in range(n-2):
        # 두 번째 격자를 놓는다. (n_row,n_col)

        for n_row in range(n):
            # 격자를 벗어나지 않을 범위로만 잡는다.
            for n_col in range(n-2):

                # 두 격자가 겹치는 경우에는 세지 않는다.
                if row == n_row and abs(column-n_col) <= 2:
                    continue

                

                # 두 격자가 겹치지 않는 경우에 대해 동전 수를 세어 갱신해준다.
                cnt1 = arr[row][column] + arr[row][column+1] + arr[row][column+2]
                cnt2 = arr[n_row][n_col] + arr[n_row][n_col+1] + arr[n_row][n_col+2]

                max_cnt = max(max_cnt,cnt1+cnt2)


print(max_cnt)

        