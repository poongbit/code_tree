n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x, y = zip(*points)
x, y = list(x), list(y)

# Please write your code here.

offset = 100


area = [[0] * 201 for _ in range(201)]



for i in range(n):
    new_x, new_y = x[i] + 100 ,y[i] + 100

    for row in range(new_x,new_x+8):
        for column in range(new_y,new_y+8):
            area[row][column] = 1


count = 0

for row in range(len(area)):
    for column in range(len(area[0])):
        if area[row][column] == 1:
            count +=1

print(count)

