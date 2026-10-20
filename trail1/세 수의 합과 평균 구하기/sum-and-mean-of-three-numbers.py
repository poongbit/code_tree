test = input().split()

num1 = int(test[0])
num2 = int(test[1])
num3 = int(test[2])

numbers = [num1,num2,num3]

print(sum(numbers))

avg = (sum(numbers)) / len(numbers)

print(int(avg))