N, B = map(int, input().split())

# Please write your code here.

digits = []

while True:
    if N < B:
        digits.append(N)
        break

    digits.append(N%B)
    N = N // B


for number in digits[::-1]:
    print(number,end="")


