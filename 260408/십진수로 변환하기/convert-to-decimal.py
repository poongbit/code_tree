binary = input()

# Please write your code here.

num = 0

for i in range(len(binary)):
    num = num * 2 + int(binary[i])

print(num)