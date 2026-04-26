n = int(input())
a, b, c = [], [], []

for _ in range(n):
    num, cnt1, cnt2 = map(int, input().split())
    a.append(num)
    b.append(cnt1)
    c.append(cnt2)

# Please write your code here.

def check_candidate(a,b,c,check_num):
    cnt1 = 0
    cnt2 = 0

    # 숫자를 꺼냄
    num = str(a)

    num_list = list(map(int,str(num)))

    for i in range(len(num_list)):
        if int(check_num[i]) == num_list[i]:
            cnt1 +=1

        elif int(check_num[i]) in num_list:
            cnt2 +=1


    if cnt1 == b and cnt2 == c:
        return 1
        
    else:
        return 0


# 결과값 저장
answer = 0

for i in range(1,10):
    for j in range(1,10):
        for k in range(1,10):
            # 세 숫자는 서로 다름
            if i != j and j !=k and i !=k:
                check_num = str(i) + str(j) + str(k)
                result = 0
                
                # n개 만큼 들어있는 힌트를 다 체크함
                for m in range(n):
                    result += check_candidate(a[m],b[m],c[m],check_num)

                # 힌트의 개수 만큼 맞아 떨어졌다면 경우의 수 추가
                if result == n:
                    answer +=1


print(answer)

                
