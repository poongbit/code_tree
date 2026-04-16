N, K, P, T = map(int, input().split())
handshakes = [tuple(map(int, input().split())) for _ in range(T)]

# Please write your code here.

graph = [[0]*(N+1) for _ in range(N+1)]

developers = []

for t,x,y in handshakes:
    developers.append((t,x,y))


developers.sort()

affected = [2] * (len(developers) + 1)

# 감기 걸린 사람들의 모임
kolok = set()

for t,row,column in developers:
    # affected가 0이 되면 영향 x
    if affected[row] == 0:
        continue

    kolok.add(column)
    affected[row] -= 1


result = [0] * (N+1)

for i in kolok:
    result[i] +=1


for i in range(1,len(result)):
    print(result[i],end="")
