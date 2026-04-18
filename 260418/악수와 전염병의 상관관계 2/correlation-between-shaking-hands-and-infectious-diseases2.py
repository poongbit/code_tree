N, K, P, T = map(int, input().split())
handshakes = [tuple(map(int, input().split())) for _ in range(T)]

# Please write your code here.

shake_num = [0] * (N+1)
infected = [False] * (N+1)

infected[P] = True

handshakes.sort()


# 각 악수 횟수를 세서,
# K번 초과로 악수를 했을 시 전염시키지 않는다.

for shakes in handshakes:
    target1 = shakes[1]
    target2 = shakes[2]

    # 감염되어 있을 경우 악수 횟수를 증가시킵니다.
    if infected[target1]:
        shake_num[target1] += 1

    if infected[target2]:
        shake_num[target2] +=1

    # target1이 감염되어 있고 아직 K번 이하로 악수했다면 target2를 전염시킴
    if shake_num[target1] <= K and infected[target1]:
        infected[target2] = True

    # target2가 감염되어 있고 아직 K번 이하로 악수했다면, target1을 전염시킨다.
    if shake_num[target2] <=K and infected[target2]:
        infected[target1] = True


for i in range(1,N+1):
    if infected[i]:
        print(1,end="")

    else:
        print(0,end="")
