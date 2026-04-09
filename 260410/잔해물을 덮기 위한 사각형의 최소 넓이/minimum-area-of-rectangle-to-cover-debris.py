x1, y1, x2, y2 = [0] * 2, [0] * 2, [0] * 2, [0] * 2
x1[0], y1[0], x2[0], y2[0] = map(int, input().split())
x1[1], y1[1], x2[1], y2[1] = map(int, input().split())

# Please write your code here.

offset = 1000

area = [[0] * 2001 for _ in range(2001)]


# 첫번째 삼각형 덮기

for row in range(x1[0] + offset, x2[0]+offset):
    for column in range(y1[0]+offset, y2[0]+offset):
        area[row][column] = 1

count = 0

for row in range(len(area)):
    for column in range(len(area[0])):
        if area[row][column] == 1:
            count +=1

# 두 번째 삼각형 덮기

mixed = 0

for row in range(x1[1]+offset ,x2[1]+offset):
    for column in range(y1[1] + offset, y2[1] + offset):
        if area[row][column] == 1:
            mixed +=1
        

if count == mixed:
    print(0)

else:
    print(count)
