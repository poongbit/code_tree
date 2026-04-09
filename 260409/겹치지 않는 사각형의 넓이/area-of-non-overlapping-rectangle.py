x1 = [1000] * 3
y1 = [1000] * 3
x2 = [1000] * 3
y2 = [1000] * 3

x1[0], y1[0], x2[0], y2[0] = map(int, input().split())
x1[1], y1[1], x2[1], y2[1] = map(int, input().split())
x1[2], y1[2], x2[2], y2[2] = map(int, input().split())

# Please write your code here.

offset = 1000

MAX_R = 2000

# 2차원 배열 선언

area = [[0]*MAX_R for _ in range(MAX_R)]


# A,B 직사각형 1로 표기하기, M 부분은 0으로 표기 

for row in range(x1[0],x2[0]):
    for column in range(y1[0],y2[0]):
        area[row][column] = 1


for row in range(x1[1], x2[1]):
    for column in range(y1[1],y2[1]):
        area[row][column] = 1


for row in range(x1[2],x2[2]):
    for column in range(y1[2],y2[2]):
        area[row][column] = 0

count = 0


for row in range(len(area)):
    for column in range(len(area[0])):
        if area[row][column] == 1:
            count +=1

print(count)