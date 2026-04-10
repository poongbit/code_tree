n, t = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.

cnt = 0
ans = 0

for i in range(n):
    if i>0 and arr[i-1]>t and (arr[i]>arr[i-1]):
        cnt +=1
    else:
        if arr[i] >t:
            cnt =1

    ans = max(ans,cnt)

print(ans)