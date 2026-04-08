n = int(input())
commands = [tuple(input().split()) for _ in range(n)]
x = []
dir = []
for num, direction in commands:
    x.append(int(num))
    dir.append(direction)

# Please write your code here.


MAX_K = 100000
#
line = [0] * (2 * MAX_K + 1)
cnt_b = [0] * (2 * MAX_K + 1)
cnt_w = [0] * (2 * MAX_K + 1)


cur = MAX_K

for i in range(n):
    dist, direction = x[i],dir[i]

    if direction == 'L':
        # 왼쪽으로 칠함
        while dist > 0:
            line[cur] = 1
            cnt_w[cur] +=1
            dist -= 1

            if dist:
                cur -= 1

    else:
        # 오른쪽으로 칠함
        while dist > 0:
            line[cur] = 2
            cnt_b[cur] +=1
            dist -=1

            if dist:
                cur +=1

g,w,b = 0,0,0

for i in range(len(line)):

    # 검은색과 흰 색 두번 이상 칠해져 있으면 회색
    if cnt_b[i] >= 2 and cnt_w[i] >=2:
        g +=1

    # 그렇지 않으면 현재 칠해진 색깔이 곧 타일의 색깔

    elif line[i] == 1:
        w +=1

    elif line[i] == 2:
        b +=1

print(w,b,g)

