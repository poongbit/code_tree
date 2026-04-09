x1, y1, x2, y2 = [0] * 2, [0] * 2, [0] * 2, [0] * 2
x1[0], y1[0], x2[0], y2[0] = map(int, input().split())
x1[1], y1[1], x2[1], y2[1] = map(int, input().split())

# Please write your code here.

offset = 1000

area = [[0] * 2001 for _ in range(2001)]


# 사각형 1,2 기록하기 

for row in range(x1[0] + offset, x2[0] + offset):
    for column in range(y1[0] + offset, y2[0] + offset):
        area[row][column] = 1

for row in range(x1[1] + offset, x2[1] + offset):
    for column in range(y1[1] + offset, y2[1] + offset):
        area[row][column] = 2


# 아직 숫자 1로 남아있는 곳들 중 최대 최소 x,y를 전부 계산

min_row,max_row,min_column,max_column = 999999,0,999999,0
first_rec_exist = False

for row in range(len(area)):
    for column in range(len(area[0])):
        if area[row][column] == 1:
            first_rect_exist = True

            min_row = min(min_row,row)
            max_row = max(max_row,row)

            min_column = min(min_column,column)
            max_column = max(max_column,column)

# 첫 번째 직사각형이 남아있지 않다면 넓이는 0

if not first_rect_exist:
    size =0

else:
    size = (max_row - min_row + 1) * (max_column - min_column + 1)
    print(size)