n = int(input())
x1, y1, x2, y2 = [], [], [], []
for _ in range(n):
    a, b, c, d = map(int, input().split())
    x1.append(a)
    y1.append(b)
    x2.append(c)
    y2.append(d)

# Please write your code here.

area = [[0] * 200 for _ in range(200)]


offset = 100

for i in range(n):
    a,b,c,d = x1[i] + offset,y1[i]+ offset,x2[i]+ offset, y2[i]+ offset
    for j in range(b,d):
        for column in range(a,c):
            area[j][column] = 1

result = 0

for i in range(len(area)):
    for j in range(len(area[0])):
        if area[i][j] == 1:
            result +=1    


print(result)
