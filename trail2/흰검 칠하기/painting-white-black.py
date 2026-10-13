n = int(input())
moves = []

for _ in range(n):
    x,d = input().split()
    moves.append((int(x),d))


OFFSET = 100000
SIZE = 2 * OFFSET + 1


# 배열 3개로 분리하기
last = [0] * SIZE
w_cnt = [0] * SIZE
b_cnt = [0] * SIZE

cur = OFFSET

for x,d in moves:
    if d == 'L':
        # 현재 타일에서 x칸 왼쪽
        for i in range(cur-x+1,cur+1):
            last[i] = 1
            w_cnt[i] +=1

        cur = cur - x +1 

    else:
        for i in range(cur,cur+x):
            last[i] = 2
            b_cnt[i] +=1

        cur = cur + x -1


white = black = gray = 0

for i in range(SIZE):
    if w_cnt[i] >=2 and b_cnt[i] >=2:
        gray +=1
    
    elif last[i] == 1:
        white +=1

    elif last[i] == 2:
        black +=1


print(white,black,gray)