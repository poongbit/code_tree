num = list(map(int,input().split()))

if num[0] > num[1]:
    print(num[0]*num[1])

else:
    print(num[1]//num[0])