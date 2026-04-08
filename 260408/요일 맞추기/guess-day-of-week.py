m1,d1,m2,d2 = map(int, input().split())

# Please write your code here.
month = [0,31,28,31,30,31,30,31,31,30,31,30,31]

first_time = 0
second_time = 0

for i in range(1,m1):
    first_time += month[i]


for j in range(1,m2):
    second_time += month[j]


first_time += d1
second_time += d2

diff = second_time - first_time

if diff < 0:
    diff += 7


date = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']

print(date[diff%7])




