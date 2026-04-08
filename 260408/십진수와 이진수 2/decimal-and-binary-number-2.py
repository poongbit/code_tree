N = input()

# Please write your code here.

# 2진수를 10진수로 바꾸기 

num = 0

for i in range(len(N)):
    num = num * 2 + int(N[i])

# 17배 곱해주기

num = num * 17

# 2. 다시 2진수로 돌리기

digits = []

while True:
    if num < 2:
        digits.append(num)
        break

    digits.append(num % 2)

    num = num // 2

for i in digits[::-1]:
    print(i,end="")
