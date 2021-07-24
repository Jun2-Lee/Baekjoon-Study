max = 1000000
check = [True]*(max+1)
count = 0
p_num = []
check[0] = check[1] = False
for i in range(2,max+1):
    if check[i] == True:
        j = i+i
        p_num.append(i)
        count += 1
        while j <=max:
            check[j] = False
            j += i
while True:
    n = int(input())
    if n == 0 :
        break
    for i in range(1,count+1):
        if check[n-p_num[i]] == True:
            print(n,'=', p_num[i] ,'+', (n - p_num[i]))
            break
"""
아리스토텔레스의 체 방법으로 소수들을 모두 구해놓은 뒤, 
입력받은 수 - 소수 를 한 수가 소수이면 출력을 하는 방식을 사용하였다.
"""
