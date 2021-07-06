num = int(input())
n_list = [0,1]
for i in range (num):
    n_list.append(n_list[i]+n_list[i+1])
print(n_list[num])
"""
N번째의 피보나치 수를 구해 출력하는 코드이다
"""
