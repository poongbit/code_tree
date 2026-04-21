n = int(input())
numbers = list(map(int, input().split()))

# Please write your code here.

result = 0

for i in range(n):
    for j in range(i+2,n):

        num = numbers[i] + numbers[j]

        result = max(result,num)


print(result)
        

