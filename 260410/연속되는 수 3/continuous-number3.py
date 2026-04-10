N = int(input())
arr = [int(input()) for _ in range(N)]

# Please write your code here.
ans = 0
cnt = 0
rev_cnt = 0

for i in range(N):
    if i>=1 and (arr[i] > 0 and arr[i-1]>0):
        cnt +=1

    elif i>=1 and (arr[i]<0 and arr[i-1]<0):
        rev_cnt +=1

    else:
        cnt = 1
        rev_cnt = 1
    ans = max(ans,cnt,rev_cnt)

print(ans)