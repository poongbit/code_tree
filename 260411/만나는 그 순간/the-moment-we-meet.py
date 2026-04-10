n, m = map(int, input().split())

d = []
t = []
for _ in range(n):
    direction, time = input().split()
    d.append(direction)
    t.append(int(time))

d2 = []
t2 = []
for _ in range(m):
    direction, time = input().split()
    d2.append(direction)
    t2.append(int(time))

# Please write your code here.

# i시간 마다 이동한 거리 체크

move_a = [0] * 1000
move_b = [0] * 1000

# 현재 누적된 시간
# 현재 위치

cur = 0
time = 0

for i in range(len(d)):
    dir, dist = d[i], t[i]

    if dir == "L":
        # dist만큼 반복
        for _ in range(dist):
            # 왼쪽으로 이동
            cur -=1

            move_a[time] = cur
            # 시간이 흐름
            time +=1

    else:
        for _ in range(dist):
            cur += 1

            move_a[time] = cur

            time +=1
    

cur = 0
time = 0

for i in range(len(d2)):
    dir, dist = d2[i], t2[i]

    if dir == "L":
        # dist만큼 반복
        for _ in range(dist):
            # 왼쪽으로 이동
            cur -=1

            move_b[time] = cur
            # 시간이 흐름
            time +=1

    else:
        for _ in range(dist):
            cur += 1

            move_b[time] = cur

            time +=1
    

for i in range(len(move_a)):
    if move_a[i] == move_b[i]:
        if move_a[i] !=0:
            print(i+1)
            break
        
        else:
            print(-1)
            break

