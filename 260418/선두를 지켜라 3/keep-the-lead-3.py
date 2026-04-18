N, M = map(int, input().split())

# Process A's movements
v = []
t = []
for _ in range(N):
    vi, ti = map(int, input().split())
    v.append(vi)
    t.append(ti)

# Process B's movements
v2 = []
t2 = []
for _ in range(M):
    vi, ti = map(int, input().split())
    v2.append(vi)
    t2.append(ti)

# Please write your code here.

MAX_T = 1000000

pos_a = [0] * (MAX_T + 1)
pos_b = [0] * (MAX_T + 1)

# A가 시간동안 이동한 거리
time_a = 1
for i in range(N):
    speed,time = v[i],t[i]

    for _ in range(time):
        pos_a[time_a] = pos_a[time_a-1] + speed
        time_a +=1

# B가 시간동안 이동한 거리
time_b = 1

for i in range(M):
    speed,time = v2[i],t2[i]

    for _ in range(time):
        pos_b[time_b] = pos_b[time_b-1] + speed
        time_b +=1


# 리더 체크하기

if pos_a[1] > pos_b[1]:
    leader = 1

elif pos_a[1] < pos_b[1]:
    leader = 2
    
else:
    # 동급인 상황
    leader = 3


max_time = max(time_a,time_b)

# 리더 바뀌는 횟수 체크
count = 1

for i in range(2,max_time):
    if pos_a[i] > pos_b[i]:
        new_lead = 1

        if leader == new_lead:
            continue

        else:
            count +=1
            leader = new_lead

    elif pos_a[i] < pos_b[i]:
        new_lead = 2

        if leader == new_lead:
            continue

        else:
            count +=1
            leader = new_lead

    else:
        new_lead = 3
        if leader == new_lead:
            continue

        else:
            count +=1
            leader = new_lead

print(count)
        
    
