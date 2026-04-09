n = int(input())
commands = [tuple(input().split()) for _ in range(n)]
x = []
dir = []
for num, direction in commands:
    x.append(int(num))
    dir.append(direction)

# Please write your code here.


MAX_K = 100000

line = [0] * (2 * MAX_K + 1)

# 왼쪽으로 하얗게 색칠한 경우
cnt_w = [0] * (2 * MAX_K + 1)

# 오른쪽으로 검정색으로 색칠한 경우
cnt_b = [0] * (2 * MAX_K + 1)



w,b,g = 0,0,0

#현재 위치
cur = MAX_K

for i in range(n):
    dist, direction = x[i],dir[i]

    if direction == 'L':
        while dist > 0:
            line[cur] = 1
            cnt_w[cur] +=1

            dist -=1

            if dist:
                cur -=1

    else:
        while dist > 0:
            line[cur] = 2
            cnt_b[cur] +=1

            dist -=1

            if dist:
                cur +=1



for i in range(len(line)):
    # 둘다 두 개 이상 색칠되어 있으면 회색
    if cnt_w[i] >= 2 and cnt_b[i] >=2:
        g +=1

    elif line[i] == 1:
        w +=1

    elif line[i] == 2:
        b +=1


print(w,b,g)

            

