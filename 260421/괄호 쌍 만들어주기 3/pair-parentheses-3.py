A = input()

# Please write your code here.

count = 0

for i in range(len(A)):
    for j in range(i,len(A)):
        if A[i] == '(' and A[j] == ')':
            count +=1

print(count)