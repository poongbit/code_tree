n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.

result = 0

for i in range(n):
    for k in range(i,n):
        max_avg = 0
        result_arr = []

        for j in range(i,k+1):
            max_avg += arr[j]
            result_arr.append(arr[j])

        max_avg /= (k+1-i)

        if max_avg in result_arr:
            result +=1


print(result)

        
