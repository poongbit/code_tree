numbers = list(map(int,input().split()))

height = numbers[0]
weight = numbers[1]

b = (10000*weight) / (height)**2

if b>=25:
    print(int(b))
    print('Obesity')

else:
    print(int(b))