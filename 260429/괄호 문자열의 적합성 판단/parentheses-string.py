str = input()

# Please write your code here.

answer = []
count = 0
flag =  True

for i in range(len(str)):
    if str[i] == '(':
        answer.append(str[i])
        

    else:
        if len(answer) != 0:
            answer.pop()
        
        else:
            flag = False
            break

    


if flag and len(answer) == 0:
    print('Yes')

else:
    print('No')


        

