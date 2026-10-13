n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.


offset = 100
line = [0] * (2*offset+1)


for a,b in segments:
    off_a = a +offset
    off_b = b + offset

    for colored in range(off_a,off_b):
        line[colored] +=1


print(max(line))
