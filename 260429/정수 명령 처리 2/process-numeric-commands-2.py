from collections import deque

N = int(input())
command = []
A = []

for _ in range(N):
    line = input().split()
    command.append(line[0])
    if line[0] == "push":
        A.append(int(line[1]))
    else:
        A.append(0)

# Please write your code here.

# 큐 선언
q = deque()

for i in range(N):
    # 명령, 숫자 입력 받기
    order, number = command[i], A[i]

    if order == 'push':
        q.append(number)

    elif order == 'front':
        print(q[0])

    elif order == 'size':
        print(len(q))

    elif order == 'empty':
        if len(q) != 0:
            print(0)

        else:
            print(1)

    elif order == 'pop':
        print(q.popleft())

