n = int(input())
S = input()

# Please write your code here.

count = 0

for i in range(n):
    if S[i] == 'C':
        for j in range(i+1,n):
            if S[j] == 'O':
                for k in range(j+1,n):
                    if S[k] == 'W':
                        count +=1

print(count)