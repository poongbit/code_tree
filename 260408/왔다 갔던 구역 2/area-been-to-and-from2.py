n = int(input())
x = []
dir = []
for _ in range(n):
    xi, di = input().split()
    x.append(int(xi))
    dir.append(di)

# Please write your code here.

OFFSET = 1000
MAX_R = 2000

# 현재 위치
cur = 0
segments = []

for j in range(n):
    dist, direction = x[j],dir[j]

    if direction == 'L':
        # 왼쪽으로 이동할 경우 : cur - distance, cur까지 경로 이동
        section_left = cur-dist
        section_right = cur
        cur -= dist

    else:
        section_left = cur
        section_right = cur + dist
        cur += dist

    segments.append([section_left,section_right])


line = [0] * (MAX_R + 1)

for x1,x2 in segments:

    # offset 더해줌
    x1,x2 = x1 + OFFSET, x2 + OFFSET

    # 구간을 칠해준다
    # 구간 단위로 진행하는 문제이므로,
    # x2에 등호가 들어가지 않음을 유의한다.

    for i in range(x1,x2):
        line[i] +=1


count = 0

for i in range(len(line)):
    if line[i] >= 2:
        count +=1

print(count)
        

