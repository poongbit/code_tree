n = int(input())
moves = [tuple(input().split()) for _ in range(n)]
dir = [move[0] for move in moves]
dist = [int(move[1]) for move in moves]

# Please write your code here.
x,y = 0,0

for i in range(n):
    direction, distance = dir[i],dist[i]

    # 동,서,남,북
    dx = [1,-1,0,0]
    dy = [0,0,-1,1]

    if direction == 'E':
        x += dx[0] * distance
        y += dy[0] * distance
    
    elif direction == 'W':
        x += dx[1] * distance
        y += dy[1] * distance

    elif direction == 'S':
        x += dx[2] * distance
        y += dy[2] * distance

    elif direction == 'N':
        x += dx[3] * distance
        y += dy[3] * distance

print(x,y)