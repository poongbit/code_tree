n, k = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.

result = 0

for i in range(n-k+1):
    max_sum = 0
    for j in range(i,i+k):
        max_sum += arr[j]

    result = max(result,max_sum)

print(result)
