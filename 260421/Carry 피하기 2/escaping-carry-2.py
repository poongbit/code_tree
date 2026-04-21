import sys
INT_MIN = -sys.maxsize

n = int(input())
arr = [int(input()) for _ in range(n)]

# Please write your code here.


# 자릿수 반환 함수
def digit_return(num,pos):
    return (num // 10 ** pos) % 10


result = INT_MIN

# 서로 다른 3개의 수를 고름

for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            
            # 숫자 3개를 지정함
            num1,num2,num3 = arr[i], arr[j], arr[k]

            max_len = max(len(str(num1)), len(str(num2)), len(str(num3)))

            not_carry = True

            for pos in range(max_len):
                if digit_return(num1,pos) + digit_return(num2,pos) + digit_return(num3,pos) >= 10:
                    not_carry = False
                    break

            if not_carry:
                num_sum = num1 + num2 + num3

                result = max(result,num_sum)



if not_carry:
    print(-1)

else:
    print(result)                 



                
