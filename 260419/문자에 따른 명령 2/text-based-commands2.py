dirs = input()

# Please write your code here.

# 원점 좌표 설정
x,y = 0,0

# 90도 회전
dx = [1,0,-1,0]
dy = [0,-1,0,1]


# 순방향
# dir_num = (dir_num + 1) % 4

# 역방향
# dir_num = (dir_num -1 + 4) % 4

# 초기는 북쪽을 바라보게 한다.
dir_num = 3

for i in range(len(dirs)):
    # 방향 결정
    direction = dirs[i]

    if direction == 'L':
        dir_num = (dir_num - 1 + 4) % 4

    elif direction == 'R':
        dir_num = (dir_num + 1) % 4

    # Forward
    else:
        x += dx[dir_num]
        y += dy[dir_num]

print(x,y)

