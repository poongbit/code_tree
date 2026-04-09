x1, y1, x2, y2 = [0] * 2, [0] * 2, [0] * 2, [0] * 2
x1[0], y1[0], x2[0], y2[0] = map(int, input().split())
x1[1], y1[1], x2[1], y2[1] = map(int, input().split())

# Please write your code here.

offset = 1000

MAX_K =  2000

# 넓이 선언
area = [[3] * (MAX_K+1) for _ in range(MAX_K +1)]

# 직사각형 1,2를 0,1로 채우기
for i in range(2):
    a,b,c,d = x1[i] + offset, y1[i] + offset, x2[i] + offset, y2[i] + offset

    for row in range(a,c):
        for column in range(b,d):
            area[row][column] = i


# 전부다 겹쳐서 1 직사각형이 없는 경우
is_rec = False

min_row,max_row,min_col,max_col = MAX_K,0,MAX_K,0


for row in range(len(area)):
    for column in range(len(area[0])):
        if area[row][column] == 0:
            # 겹치는 부분이 있음
            is_rec = True
            min_row = min(min_row,row)
            max_row = max(max_row,row)
            min_col = min(min_col,column)
            max_col = max(max_col,column)


if not is_rec:
    size = 0

else:
    size = (max_row-min_row + 1) * (max_col - min_col + 1)

print(size)
