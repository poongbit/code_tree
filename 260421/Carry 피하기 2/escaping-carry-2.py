import sys
INT_MIN = -sys.maxsize

n = int(input())
arr = [int(input()) for _ in range(n)]

# Please write your code here.

def digit_number(num,pos):
    return (num // 10 ** pos) % 10

# 가장 큰 값 저장할 변수 생성 
result = INT_MIN

# 실제로 carry가 발생하는 조합이 있는 지 체크
found = False

# 숫자 3개 고르기

for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):

            # 숫자 3개 선택 
            num1, num2, num3 = arr[i], arr[j], arr[k]

            # 각 자릿수 뽑기

            # 숫자들 중 가장 긴 숫자 찾기

            max_len = max(len(str(num1)), len(str(num2)), len(str(num3)))

            is_carry = False

            for p in range(max_len):
                if digit_number(num1,p) + digit_number(num2,p) + digit_number(num3,p) >= 10:
                    is_carry = True
                    break

            if is_carry:
                continue

            else:
                found = True
                num_sum = num1 + num2 + num3
                result = max(result,num_sum)


if found:
    print(result)

else:
    print(-1)

                
