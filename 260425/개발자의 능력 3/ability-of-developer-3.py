abilities = list(map(int, input().split()))

# Please write your code here.

def get_result(i,j,k):
    sum1 = abilities[i] + abilities[j] + abilities[k]

    sum2 = sum(abilities) - sum1

    return abs(sum1-sum2)

min_result = 1000000

for i in range(0,6):
    for j in range(i+1,6):
        for k in range(j+1,6):

            min_result = min(min_result,get_result(i,j,k))

    
print(min_result)

