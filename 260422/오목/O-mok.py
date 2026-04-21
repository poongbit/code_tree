board = [list(map(int, input().split())) for _ in range(19)]

# Please write your code here.

# 오른쪽, 아래, 오른쪽 아래 대각선, 왼쪽 아래 대각선
d_row = [0,1,1,1]
d_col = [1,0,1,-1]


# 똑같은 방향에서 계속 같은 색인지
def check_dir(row,col,index,color):

    count = 0

    while count < 4:
        n_row,n_col = row + d_row[index], col + d_col[index]

        if board[n_row][n_col] == color:
            count +=1

            row,col = n_row,n_col
            continue

        else:
            break

    if count ==4:
        return True

    else:
        return False

# 승부가 낫는 지 체크
shobu = False

# 승부가 난 row,column 수집
answer = []

for row in range(19):
    for column in range(19):
        
        # 시작점이 흰색 알일 경우

        if board[row][column] == 1:

            # 오른쪽,아래,오른쪽 대각선, 왼쪽 대각선 중 어느 인덱스가 작동되는 지 체크

            for index in range(4):
                if check_dir(row,column,index,1):
                    shobu = True
                    answer.append((row,column,index))
                    break

        elif board[row][column] == 2:
            for index in range(4):
                if check_dir(row,column,index,2):
                    shobu = True
                    answer.append((row,column,index))
                    break

        
        if shobu:
            break


if shobu:
    for row,column,index in answer:
        print(board[row][column])
        
        n_row, n_col = row + 2 * d_row[index], column + 2 * d_col[index]

        print(n_row+1,n_col+1)
    
else:
    print(0)
