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
cnt_w = 0
cnt_b = 0


# 왼쪽으로 뒤집으면 흰 색 1, 오른쪽은 검은색 2

cur = MAX_K

for i in range(n):
    dist, direction = x[i], dir[i]

    if direction == 'L':
        while dist > 0:
            line[cur] = 1
            
            dist -=1

            if dist:
                cur -=1


    else:
        while dist > 0:
            line[cur] = 2
            dist -=1

            if dist:
                cur +=1


for i in range(len(line)):
    if line[i] == 1:
        cnt_w +=1

    elif line[i] == 2:
        cnt_b +=1

print(cnt_w,cnt_b)
        
