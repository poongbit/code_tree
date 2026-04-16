n, m = map(int, input().split())

# Process robot A's movements
t = []
d = []
for _ in range(n):
    time, direction = input().split()
    t.append(int(time))
    d.append(direction)

# Process robot B's movements
t_b = []
d_b = []
for _ in range(m):
    time, direction = input().split()
    t_b.append(int(time))
    d_b.append(direction)

# Please write your code here.

MAX_T = 1000000

a_time = [0] * (MAX_T +1)
b_time = [0] * (MAX_T +1)

# A의 움직임 기록
time_a =1

for i in range(n):
    time,direction = t[i],d[i]

    if direction == 'R':
        for _ in range(time):
            a_time[time_a] = a_time[time_a-1] + 1
            time_a +=1

    else:
        for _ in range(time):
            a_time[time_a] = a_time[time_a-1] -1
            time_a +=1

        
time_b = 1

for i in range(m):
    time, direction = t_b[i], d_b[i]

    if direction == 'R':
        for _ in range(time):
            b_time[time_b] = b_time[time_b-1] +1
            time_b +=1

        
    else:
        for _ in range(time):
            b_time[time_b] = b_time[time_b-1] -1
            time_b +=1

count = 0

max_time = max(time_a-1,time_b-1)

# A 루프 끝난 후

for i in range(time_a,max_time +1):
    a_time[i] = a_time[time_a-1] # 마지막 위치 그대로 있기


for j in range(time_b,max_time+1):
    b_time[j] = b_time[time_b-1] #마지막 위치 그대로 있기


for i in range(1,max_time+1):
    if a_time[i-1] != b_time[i-1] and a_time[i] == b_time[i]:
        count +=1

print(count)