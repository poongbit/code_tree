N = int(input())
a1, b1, c1 = map(int, input().split())
a2, b2, c2 = map(int, input().split())

# Please write your code here.

count = 0

def circular_dist(x,y,N):
    d = abs(x - y)
    return min(d, N-d) # 직선 거리 vs 돌아가는 거리


for i in range(1,N+1):
    for j in range(1,N+1):
        for k in range(1,N+1):
            if circular_dist(a1,i,N) <=2 and circular_dist(b1,j,N) <=2 and circular_dist(c1,k,N)<=2:
                count +=1
                continue

            elif circular_dist(a2,i,N)<=2 and circular_dist(b2,j,N)<=2 and circular_dist(c2,k,N)<=2:
                count +=1
                continue

print(count)