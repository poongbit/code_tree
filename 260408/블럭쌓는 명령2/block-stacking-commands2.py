n, k = map(int, input().split())
commands = [tuple(map(int, input().split())) for _ in range(k)]

# Please write your code here.

area = [0] * (n+1)

for start,end in commands:
    for i in range(start,end+1):
        area[i] +=1

print(max(area))
