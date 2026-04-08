n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.

line = [0] * (2*100 + 1)

offset = 100

for x1,x2 in segments:
    off_x1 = x1 + offset
    off_x2 = x2 + offset

    for i in range(off_x1,off_x2):
        line[i] +=1


print(max(line))

