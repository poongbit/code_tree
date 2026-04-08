n = int(input())
x = []
dir = []
for _ in range(n):
    xi, di = input().split()
    x.append(int(xi))
    dir.append(di)

# Please write your code here.

line = [0] * 101
start_pos = 10

for i in range(n):
    move,direction = x[i],dir[i]

    if direction == 'R':
        for j in range(start_pos,start_pos + move):
            line[j] +=1

        start_pos += move

    elif direction == 'L':

        for k in range(start_pos,start_pos-move,-1):
            line[k] +=1

        start_pos -= move



count = 0

for i in range(len(line)):
    if line[i] >= 2:
        count +=1

print(count)
        

