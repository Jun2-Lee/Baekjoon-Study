max = 1000000
check = [True]*(max+1)
check[0] = check[1] = False
p_num = []
count = 0
for i in range(2,max+1):
    if check[i] == True:
        j = i+i
        p_num.append(i)
        count += 1
        while j <= max:
            check[j] = False
            j += i
while(True):
    N = int(input())
    if N == 0:
        break
    i = 1
    while i < count:
        if check[N-p_num[i]] == True and N-p_num[i]>0 and N-p_num[i] != 2:
            print(N,'=',p_num[i],'+',N-p_num[i])
            break
        i += 1
    if i == count:
        print("Goldbach's conjecture is wrong.")
"""
아리스토텔레스의 체 방법으로 소수들을 모두 구해놓은 뒤, 
입력받은 수 - 소수 를 한 수가 소수이면 출력을 하는 방식을 사용하였다.
또, 두 홀수 소수의 합으로 n을 나타낼 수 없는 경우에는
"Goldbach's conjecture is wrong."을 출력한다.
"""
