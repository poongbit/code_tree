N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# Please write your code here.

# 탐색할 arr의 길이 설정
k = len(B)

B.sort()


count = 0

for i in range(N-k+1):
    # 결과를 담을 배열 선언
    arr = []
    for j in range(i,i+k):
        arr.append(A[j])

    arr.sort()

    if B == arr:
        count +=1


print(count)
