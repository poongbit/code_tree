n = int(input())
grid = [list(input()) for _ in range(n)]
k = int(input())

# Please write your code here.

"""
남쪽에서 쐈을 떄 : / - left, \ - right
북쪽에서 쐈을 때 : / - right, \ - left
동쪽에서 쐈을 때 : / - down, , \ - up
서쪽에서 쐈을 때 : / - up, \ - down

"""

# 주어진 숫자에 따라
# 시작 위치와 방향을 구한다

def initialize(num):
    if num <=n:
        return 0, num -1, 0
    elif num <= 2 * n:
        return num -n -1, n-1,1

    elif num <=3 * n:
        return n-1, n-(num-2*n), 2

    else:
        return n - (num - 3 * n),0,3



def in_range(row,column):
    return 0 <= row < n and 0<=column<n

# (x,y)에서 시작하여 next_dir 방향으로
# 이동한 이후의 위치를 반환한다.

def move(row,column,next_dir):
    d_row, d_column = [1,0,-1,0], [0,-1,0,1]
    n_row,n_col = row + d_row[next_dir], column + d_column[next_dir]

    return n_row, n_col, next_dir


def simulate(row,column,move_dir):
    move_num = 0

    while in_range(row,column):
        # 0 <-> 1 / 2 <-> 3
        if grid[row][column] == '/':
            row,column,move_dir = move(row,column,move_dir^1)
        # 0 <-> 3 / 1 <-> 2
        else:
            row,column,move_dir = move(row,column,3 - move_dir)
        
        move_num +=1

    return move_num


# 시작 위치와 방향을 구한다
row,column, move_dir = initialize(k)

#(row,column)에서 move_dir 방향으로 시작하여
# 시뮬레이션 진행
move_num = simulate(row,column,move_dir)
print(move_num)