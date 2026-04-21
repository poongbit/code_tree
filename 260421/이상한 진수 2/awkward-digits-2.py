import sys
INT_MIN = -sys.maxsize

a = list(map(int,input()))
# Please write your code here.

# 2-digits로 변환하기

result = 0

for i in range(1,len(a)):
    origin = a[i]

    # 0 ->1 / 1->0 변환
    a[i] = (a[i]+1) % 2

    num = 0
    for j in range(len(a)):
        num = num * 2 + a[j]

    result = max(result,num)

    a[i] = origin

print(result)