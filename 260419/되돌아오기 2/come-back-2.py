commands = input()

# Please write your code here.

# 90도 회전
# 동,남,서,북
dx = [1,0,-1,0]
dy = [0,-1,0,1]

# 원점 선언
x,y = 0,0
move_dir = 3

# 시간 기록
time = 0

# 되돌아욌는 지?
is_returned = False

for i in range(len(commands)):
    dir = commands[i]

    if dir == 'L':
        move_dir = (move_dir -1 + 4) % 4
        time +=1

    elif dir == 'R':
        move_dir = (move_dir + 1) % 4
        time +=1

    else:
        x = x + dx[move_dir]
        y = y + dy[move_dir]

        time +=1

        if x ==0 and y == 0:
            is_returned = True
            print(time)
            break


if not is_returned:
    print(-1)
    
    

        