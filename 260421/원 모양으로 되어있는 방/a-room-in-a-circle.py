import sys
INT_MAX = sys.maxsize

n = int(input())
a = [int(input()) for _ in range(n)]

# Please write your code here.

min_distance = INT_MAX

for i in range(n):
    # 시작 지점을 기준으로 완전 탐색 
    start_position = i
    result = 0

    for j in range(1,n):
        start_position = (start_position + 1) % n

        result += j * a[start_position]

    
    min_distance = min(min_distance,result)
        
        
        
print(min_distance)
