import sys
INT_MAX = sys.maxsize

N, S = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.

min_result = INT_MAX

for i in range(N-1):
    for j in range(i+1,N):
        origin_1, origin_2 = arr[i],arr[j]
        
        # 0으로 초기화
        arr[i], arr[j] = 0,0

        T = 0

        for k in range(len(arr)):
            T += arr[k]

            result = abs(T-S)

        min_result = min(min_result,result)

        # 다시 원상 복구
        arr[i],arr[j] = origin_1, origin_2


print(min_result)

        
