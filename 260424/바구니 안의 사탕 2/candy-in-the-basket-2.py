N, K = map(int, input().split())
candy = []
pos = []

for _ in range(N):
    c, p = map(int, input().split())
    candy.append(c)
    pos.append(p)

# Please write your code here.

MAX_K = 500

locate = [0] * (MAX_K + 10)

# 사탕의 개수와 위치 기록하기 
for i in range(N):
    locate[pos[i]] = candy[i]

result = 0


for i in range(1,MAX_K - K + 2):
    max_candy = 0
    for c in range(i-K, i+K+1):
        max_candy += locate[c]

    result = max(result,max_candy)

print(result)
