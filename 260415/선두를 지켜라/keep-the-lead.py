n, m = map(int, input().split())

# Process A's movements
v = []
t = []
for _ in range(n):
    vi, ti = map(int, input().split())
    v.append(vi)
    t.append(ti)

# Process B's movements
v2 = []
t2 = []
for _ in range(m):
    vi, ti = map(int, input().split())
    v2.append(vi)
    t2.append(ti)

# Please write your code here.

MAX_T = 100000

a_time = [0] * (MAX_T + 5)
b_time = [0] * (MAX_T + 5)

# A가 매 초 서 있는 위치 기록
time_a = 1

for i in range(n):
    speed,time = v[i],t[i]
    for _ in range(time):
        a_time[time_a] = a_time[time_a -1] + speed
        time_a +=1


# B가 매 초마다 서 있는 위치를 기록
time_b = 1

for i in range(m):
    v,t = v2[i],t2[i]
    for _ in range(t):
        b_time[time_b] = b_time[time_b-1] + v
        time_b += 1

# A와 B 중 더 앞서 있는 경우를 확인한다.
leader, ans = 0,0

for i in range(1,time_a):
    if a_time[i] > b_time[i]:
        # 기존 리더가 B였다면
        # 답을 갱신한다
        if leader == 2:
            ans +=1

        
        leader = 1

    elif a_time[i] < b_time[i]:
        # 기존 리더가 A였다면
        # 답을 갱신한다
        if leader == 1:
            ans +=1

        # 리더를 B로 변경한다

        leader = 2

print(ans)
