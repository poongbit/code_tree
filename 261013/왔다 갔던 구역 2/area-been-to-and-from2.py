n = int(input())

moves = []

for i in range(n):
    data = input().split()

    distance = data[0]
    dir = data[1]
    moves.append((int(distance),dir))


OFFSET = 1000
line = [0] * (2*OFFSET)

# 0을 OFFSET으로 맵핑
cur = OFFSET

for dist, dir in moves:
    if dir == 'R':
        for colored in range(cur,cur+dist):
            line[colored] +=1

        cur += dist

    else:
        for colored in range(cur-dist,cur):
            line[colored] +=1
        cur -= dist


result = 0

for i in range(len(line)):
    if line[i] >=2:
        result +=1

print(result)


