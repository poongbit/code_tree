numbers = input().split()

num = [int(numbers[0]),int(numbers[1]),int(numbers[2])]

print(sum(num))
print(int(sum(num)/len(num)))
print(sum(num) - int(sum(num)/len(num)) )