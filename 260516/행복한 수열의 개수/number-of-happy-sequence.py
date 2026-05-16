n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

sequence = [0 for _ in range(n)]

def is_happy_sequence():
    # 주어진 seq가 행복한 수열인지 판단하는 함수

    consec_cnt, max_cnt = 1,1

    for i in range(1,n):
        if seq[i-1] == seq[i]:
            consec_cnt +=1

        else:
            consec_cnt = 1

        max_cnt = max(max_cnt, consec_cnt)

    return max_cnt >= m


num_happy = 0

# 먼저 가로로 행복한 수열의 수를 센다

for i in range(n):
    seq = grid[i][:]

    if is_happy_sequence():
        num_happy +=1


# 세로로 행복한 수열의 수를 센다

for j in range(n):
    # 세로로 숫자들을 모아 새로운 수열을 만든다.

    for i in range(n):
        seq[i] = grid[i][j]

    if is_happy_sequence():
        num_happy +=1


print(num_happy)



        

        
        
