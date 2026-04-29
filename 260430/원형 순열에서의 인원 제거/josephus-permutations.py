from collections import deque

n, k = map(int, input().split())

# Please write your code here.

number = [i for i in range(1,n+1)]

q = deque(number)


while q:
    for i in range(k-1):
        num = q.popleft()

        q.append(num)

    print(q.popleft(),end = " ")
    
    