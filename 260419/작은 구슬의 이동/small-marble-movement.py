n, t = map(int, input().split())
r, c, dir = input().split()
r, c = int(r), int(c)

# Please write your code here.

# 0번,3번이 반대가 되게, 1번과 2번이 반대가 되게 함
# 상,좌,우,하
dx = [0,-1,1,0]
dy = [-1,0,0,1]


d = {} # dict 초기화

d['R'] = 2
d['D'] = 3
d['U'] = 0
d['L'] = 1


dir_num = d[dir]


def in_range(row,column):
    return 0<= row <n and 0<= column <n

# 초기 좌표
row,column = r,c
time = 0


while time <= t+1:
    time +=1
    n_row = row + dy[dir_num]
    n_column = column + dx[dir_num]

    if not in_range(n_row,n_column):
        dir_num = 3 - dir_num # change direction
        continue

    # move 
    row, column = row + dy[dir_num], column + dx[dir_num]
    

print(row,column)

