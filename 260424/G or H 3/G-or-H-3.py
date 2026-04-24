n, k = map(int, input().split())
x = []
c = []
for _ in range(n):
    pos, char = input().split()
    x.append(int(pos))
    c.append(char)

# Please write your code here.

# G가 찍히면 1점, H가 찍히면 2점, 최대 점수를 구하라

result = [0] * (10005)

for i in range(n):
    result[x[i]] = c[i]

answer = 0

for i in range(1,10001-k+2):
    max_result = 0

    for j in range(i,i+1+k):
        if result[j] == 'G':
            max_result += 1

        elif result[j] == 'H':
            max_result += 2

        else:
            continue


    answer = max(answer,max_result)

print(answer)
    



    

