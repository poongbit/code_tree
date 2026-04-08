m1,d1,m2,d2 = map(int, input().split())

# Please write your code here.
month = [0,31,28,31,30,31,30,31,31,30,31,30,31]

first_time = month[m1] + d1
second_time = month[m2] + d2

result = abs(first_time - second_time)


date = [0,'Sun','Mon','Tue','Wed','Thu','Fri','Sat']


print(date[result % 7])