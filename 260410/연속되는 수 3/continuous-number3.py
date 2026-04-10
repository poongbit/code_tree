N = int(input())
arr = [int(input()) for _ in range(N)]

# Please write your code here.
result = []

yang = 1
umm = 1

for i in range(N):

    if i>0 and (arr[i]>0 and arr[i-1]>0):
        yang +=1
        result.append(umm)
        umm = 1

    elif i == 0:
        if arr[i] >0:
            yang +=1
        else:
            umm +=1

    elif i > 0 and (arr[i]<0 and arr[i-1]<0):
        umm +=1
        result.append(yang)
        yang = 1


print(max(result))

