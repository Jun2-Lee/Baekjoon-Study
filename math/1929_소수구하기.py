max = 1000000
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
M,N = map(int, input().split())
for i in range(M,N+1):
    if check[i]==True:
        p_num.append(i)
print('\n'.join(map(str,p_num)))

"""
앞의 1978번에서 사용했던 아리스토텔레스의 체 방법을 이용해서
max까지의 소수들을 모두 구해놓은 뒤, 입력받은 범위에 소수가 있는지 판별하는 방법을 사용했다.
"""
