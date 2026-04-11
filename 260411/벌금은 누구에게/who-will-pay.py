N, M, K = map(int, input().split())
student = [int(input()) for _ in range(M)]

# Please write your code here.

punishment = [0] * (len(student) +1)

for member in student:
    # 벌점 기록

    punishment[member] +=1

    if punishment[member] == K:
        print(member)