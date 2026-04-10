n = int(input())
arr = [int(input()) for _ in range(n)]

# Please write your code here.
#연속해서 동일한 숫자가 나오는 횟수를 구한다
# 그 중 최댓값을 갱신한다

ans,cnt = 0,0

for i in range(n):
    # 연속해서 나올 경우

    if i>= 1 and arr[i] == arr[i-1]:
        cnt +=1

    else:
        # 다시 초기화
        cnt = 1

    ans = max(ans,cnt)

print(ans)
    
    

