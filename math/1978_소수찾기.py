max = 1000
check = [True]*(max+1)
count = 0
p_num = []
check[0] = check[1] = False
for i in range(2,max+1):
    if check[i] == True:
        j = i+i
        while j <=max:
            check[j] = False
            j += i
N = int(input())
n_list = list(map(int,input().split()))
for i in range(N):
    if check[n_list[i]] == True:
        count += 1
print(count)

"""
part1 부분에 있는 문제와 같은 문제지만,
이번에는 입력을 받은 뒤 소수를 판별하는 것이 아닌
1000까지 모든 소수를 구해놓은 뒤 입력받은 수가 소수인지 판별하였다.
아리스토텔레스의 체 방법을 이용했다. 
"""
