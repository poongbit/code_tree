n = int(input())
arr = [int(input()) for _ in range(n)]

# Please write your code here.

cnt = 0


def check_num(arr):
    n = len(arr)
    cnt_arr = []
    cnt = 0

    if n == 1:
        cnt_arr.append(1)

    for i in range(n):
        if i == 0:
            cnt += 1
    
        elif arr[i] != arr[i-1]:
            cnt_arr.append(cnt)
            cnt = 0
            cnt +=1
        
        else:
            cnt +=1

    
    return cnt_arr

result = check_num(arr)

print(max(result))