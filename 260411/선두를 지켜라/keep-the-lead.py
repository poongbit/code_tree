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

a_time = [0] * 1001
b_time = [0] * 1001

cur = 0
spent = 0
# A의 움직임 
for i in range(len(v)):
    speed,time = v[i],t[i]

    for k in range(spent+1,spent + time+1):
        cur += speed
        a_time[k] = cur

    spent += time

cur2 = 0
spent = 0
for j in range(len(v2)):
    speed,time = v2[j],t2[j]

    for m in range(spent+1,spent + time+1):
        cur2 += speed
        b_time[m] 

    spent += time


lead = [0] * 1001

count = 0

for i in range(1,len(a_time)):

    if a_time[i] > b_time[i]:
        lead[i] = 1

    elif a_time[i] < b_time[i]:
        lead[i] = 2
    

    if lead[i] != lead[i-1]:
        count +=1


print(count)
