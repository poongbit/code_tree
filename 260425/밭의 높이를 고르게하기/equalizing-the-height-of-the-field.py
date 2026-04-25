N, H, T = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.

min_result = 999999

for i in range(N):
    # 구간 범위 설정
    for j in range(i,N):
        # 담을 구간 설정
        # 최소 T 구간 이상 작동
        cost = 0
        
        if j - i + 1 >= T:
            for k in range(i,j+1):
                cost += abs(arr[k]- H)
        
            min_result = min(min_result,cost)

print(min_result)