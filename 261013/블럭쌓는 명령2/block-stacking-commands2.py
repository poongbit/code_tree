n, k = map(int, input().split())
commands = [tuple(map(int, input().split())) for _ in range(k)]

# Please write your code here.

blocked = [0] * n

for start,end in commands:
    for colored in range(start-1,end):
        blocked[colored] +=1


max_result = 0

for item in blocked:
    if item >= max_result:
        max_result = item


print(max_result)