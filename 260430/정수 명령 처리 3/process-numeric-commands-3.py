from collections import deque
n = int(input())
cmd = []
num = []

for _ in range(n):
    line = input().split()
    cmd.append(line[0])
    if line[0] in ["push_front", "push_back"]:
        num.append(int(line[1]))
    else:
        num.append(0)

# Please write your code here.

q = deque()

for i in range(n):
    order, number = cmd[i],num[i]

    if order == 'push_back':
        q.append(number)

    elif order == 'push_front':
        q.appendleft(number)

    elif order == 'pop_front':
        print(q.popleft())

    elif order == 'front':
        print(q[0])

    elif order == 'pop_back':
        print(q.pop())

    elif order == 'size':
        print(len(q))

    elif order == 'empty':
        if len(q) != 0:
            print(0)

        else:
            print(1)

    elif order == 'back':
        print(q[-1])

