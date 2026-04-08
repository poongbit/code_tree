n = int(input())

# Please write your code here.

digit = []

while True:
    # n이 2보다 작으면 append 후 break
    if n < 2:
        digit.append(n)
        break

    digit.append(n%2)
    n = n // 2


for number in digit[::-1]:
    print(number, end="")