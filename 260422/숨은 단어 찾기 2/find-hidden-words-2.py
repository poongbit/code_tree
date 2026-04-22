import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [input().strip() for _ in range(N)] 

# Please write your code here.

# 위,왼쪽 위 대각선, 왼쪽, 왼쪽 아래 대각선, 아래, 오른쪽 아래 대각선
# 오른쪽, 오른쪽 위 대각선
d_row = [-1,-1,0,1,1,1,0,-1]
d_col = [0,-1,-1,-1,0,1,1,1]


# 안에 벗어나지 않는 지 확인하기
def in_range(row,col):
    return 0<=row<N and 0<=col<M

# 계속 나아가서 확인하기
def word_check(row,col,index,word):
    count = 1
    while count <3 :
        n_row,n_col = row + d_row[index], col + d_col[index]

        if in_range(n_row,n_col) and arr[n_row][n_col] == word[count]:
            count +=1
            row,col = n_row,n_col

        else:
            break
    
    if count == 3:
        return True

    else:
        return False

result = 0

for row in range(N):
    for column in range(M):
        if arr[row][column] != 'L':
            continue

        for index in range(8):
            if word_check(row,column,index,'LEE'):
                result +=1


print(result)


                


