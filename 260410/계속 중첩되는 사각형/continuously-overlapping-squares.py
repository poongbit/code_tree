n = int(input())
x1, y1, x2, y2 = [], [], [], []
for _ in range(n):
    a, b, c, d = map(int, input().split())
    x1.append(a)
    y1.append(b)
    x2.append(c)
    y2.append(d)

# Please write your code here.

offset = 100
MAX_K = 200

area = [[0] * (MAX_K+1) for _ in range(MAX_K+1)]


for i in range(n):
    a,b,c,d = x1[i] + offset, y1[i] + offset, x2[i] + offset, y2[i] + offset


    for row in range(a,c):
        for column in range(b,d):
            area[row][column] = 1 if i % 2 == 0 else 2

count = 0

for row in range(len(area)):
    for column in range(len(area[0])):
        if area[row][column] == 2:
            count +=1


print(count)