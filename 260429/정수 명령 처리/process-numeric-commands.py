N = int(input())
command = []
value = []

for _ in range(N):
    line = input().split()
    command.append(line[0])
    if line[0] == "push":
        value.append(int(line[1]))
    else:
        value.append(0)

# Please write your code here.

# 빈 리스트 생성
answer = []


for i in range(N):
    order, val = command[i],value[i]

    if order == 'push':
        answer.append(val)

    elif order == 'size':
        print(len(answer))

    elif order == 'pop':

        print(answer.pop())

    elif order == 'empty':
        if len(answer) == 0:
            print(1)

        else:
            print(0)
    elif order == 'top':

        print(answer[-1])


    