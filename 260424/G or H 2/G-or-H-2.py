n = int(input())
people = [tuple(input().split()) for _ in range(n)]
pos = [int(p[0]) for p in people]
alpha = [p[1] for p in people]

# Please write your code here.

MAX_N = 100

paired = sorted(zip(pos, alpha))  # (위치, 알파벳) 묶어서 정렬
pos = [p[0] for p in paired]
alpha = [p[1] for p in paired]

locate = [0] * (MAX_N + 1)

# locate 배열에 위치시킴
for i in range(n):
    locate[pos[i]] = alpha[i]

answer = 0

# 모든 구간 탐색
for i in range(n):
    for j in range(i,n):
        max_length = []

        for k in range(i,j+1):
            max_length.append((pos[k],locate[pos[k]]))

        g_count = 0
        h_count = 0
        
        result = []

        for index,item in max_length:
            if item == 'G':
                g_count +=1
                result.append(index)
            
            elif item == 'H':
                h_count +=1
                result.append(index)
        
        if g_count == h_count and len(result) > 0:
            answer = max(answer, result[-1] - result[0])

        elif (g_count !=0 and h_count == 0) or (g_count == 0 and h_count !=0):
            answer = max(answer, result[-1] - result[0])


print(answer)




