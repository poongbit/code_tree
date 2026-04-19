N = int(input())
moves = [tuple(input().split()) for _ in range(N)]
dir = [move[0] for move in moves]
dist = [int(move[1]) for move in moves]

# Please write your code here.

# 원점 스타트
x,y = 0,0

# 동,서,남,북
dx = [1,-1,0,0]
dy = [0,0,-1,1]


mapping = {
    'E' : 0,
    'W' : 1,
    'S' : 2,
    'N' : 3
}

time = 1
is_exist = False
for i in range(N):
    direction,distance = dir[i],dist[i]
    dir_index = mapping[direction]

    for _ in range(distance):
        
        x = x + dx[dir_index] 
        y = y + dy[dir_index]
        
        if x == 0 and y == 0:
            is_exist = True
            break
        else:
            time +=1

    if is_exist:
        print(time)
        break

    
if not is_exist:
    print(-1)

