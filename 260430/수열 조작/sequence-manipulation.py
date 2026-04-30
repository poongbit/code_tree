from collections import deque

n = int(input())

# Please write your code here.
number = [i for i in range(1,n+1)]

q = deque(number)

while len(q) != 1:
    
    q.popleft()

    q.append(q.popleft())

print(q[0])
