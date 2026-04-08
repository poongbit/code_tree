m1, d1, m2, d2 = map(int, input().split())
A = input()

# Please write your code here.

month = [31,28,31,30,31,30,31,31,30,31,30,31]

# A의 인덱스 위치 파악하기
day_of_week = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']

A_index = 0

for i in range(len(day_of_week)):
    if A == day_of_week[i]:
        A_index = i
        break



count = 0

# 시작 요일은 월요일
start_index = 0

while True:
    if m1 == m2 and d1 == d2:
        break
    d1 +=1

    # 인덱스 증가 가능 여부 체크 

    start_index %=7

    if start_index == A_index:
        count +=1
    
    start_index += 1

    if d1 > month[m1]:
        m1 +=1
        d1 = 1

    
print(count)