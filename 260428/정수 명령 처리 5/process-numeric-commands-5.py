N = int(input())

command = []
num = []

for _ in range(N):
    line = input().split()
    command.append(line[0])
    if line[0] == "push_back" or line[0] == "get":
        num.append(int(line[1]))
    else:
        num.append(0)

# Please write your code here.

answer = []

for i in range(N):
    order, number = command[i], num[i]
    if order == 'push_back':
        answer.append(number)

    elif order == 'get':
        print(answer[number-1])

    elif order == 'size':
        print(len(answer))

    elif order == 'pop_back':
        answer.pop()

    
