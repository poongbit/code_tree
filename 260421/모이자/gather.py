import sys
INT_MAX = sys.maxsize

n = int(input())
A = list(map(int, input().split()))

# Please write your code here.

min_val = INT_MAX

for i in range(n):
    origin = A[i]
    sum = 0
    # 목표 지점이므로 거리는 0
    A[i] = 0

    for j in range(n):
        distance = abs(i-j)
        sum += distance * A[j]

    min_val = min(min_val,sum)

    A[i] = origin


print(min_val)
