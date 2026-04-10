n = int(input())
arr = [int(input()) for _ in range(n)]

# Please write your code here.

cnt = 1
connected = []

for i in range(n):
    if i == 0 or arr[i] != arr[i-1]:
        connected.append(cnt)
        cnt = 1

    else:
        cnt +=1

print(max(connected))

    
    

