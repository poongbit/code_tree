a, b = map(int, input().split())
n = input()

# Please write your code here.

# a진수를 10진수로 바꿔주기

number = str(n)
num = 0

for i in range(len(number)):
    num = num * a + int(number[i])


# 10진수를 b진수로 바꿔주기 
digits = []

while True:
    if num < b:
        digits.append(num)
        break

    digits.append(num % b)

    num = num // b

for i in digits[::-1]:
    print(i,end="")

