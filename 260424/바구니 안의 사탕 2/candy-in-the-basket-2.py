N, K = map(int, input().split())
candy = []
pos = []

for _ in range(N):
    c, p = map(int, input().split())
    candy.append(c)
    pos.append(p)

# Please write your code here.

MAX_K = 100

locate = [0] * (MAX_K + 1)

# 사탕의 개수와 위치 기록하기 
for i in range(N):
    locate[pos[i]] += candy[i]

result = 0


for i in range(0,MAX_K):
    max_candy = 0
    for c in range(i-K,i+K+1):
        # 주어진 위치가 넘어가서는 안된다
        if c >=0 and c <= MAX_K:
            max_candy += locate[c]

    result = max(result,max_candy)

print(result)
