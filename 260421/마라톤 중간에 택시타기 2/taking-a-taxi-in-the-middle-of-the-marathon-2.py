import sys
INT_MAX = sys.maxsize

n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]

# Please write your code here.

# 시작 지점 기록
start_x, start_y = x[0],y[0]
end_x,end_y = x[n-1],y[n-1]

min_distance = INT_MAX

for i in range(1,n-1):
    origin_x, origin_y = x[i],y[i]

    # 전에 위치랑 같게 해줌
    x[i],y[i] = x[i-1],y[i-1]

    # 거리 초기화
    distance = 0

    for j in range(n-1):
        distance += abs(x[j+1]-x[j]) + abs(y[j+1]-y[j])
    
    min_distance = min(min_distance, distance)

    # 원상 복구
    x[i],y[i] = origin_x, origin_y



print(min_distance)
