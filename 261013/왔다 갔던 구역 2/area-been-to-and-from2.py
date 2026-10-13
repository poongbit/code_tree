n = int(input())
moves = []
for _ in range(n):
    xi, di = input().split()
    moves.append((int(xi),di))

# Please write your code here.

# 음수 좌표 -> offset으로 평행이동해서 배열 인덱스로 사용
OFFSET = 1000
line = [0] * (2*OFFSET +1)

cur = OFFSET # 현재 위치 (0을 OFFSET으로 매칭)

for dist,d in moves:
    if d == 'R':
        # 구간 [cur,cur+dist) 칠하기 
        for i in range(cur,cur+dist):
            line[i] +=1
        cur += dist

    else:
        # 구간 [cur-dist,cur) 만큼 칠하기
        for i in range(cur-dist,cur):
            line[i] +=1
        cur -= dist

result = 0

for i in range(len(line)):
    if line[i] >=2:
        result +=1

print(result)



