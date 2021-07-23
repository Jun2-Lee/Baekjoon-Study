N = int(input())
res = 0
for i in range(1,N+1):
    for j in range(1,i+1):
        if(i%j == 0):
            res += j
print(res)

"""
1부터 N까지의 모든 약수들의 합을 구하는 코드이다. 
하지만, 시간복잡도가 O(N^2)이기 때문에 문제에서는 시간 초과가 난다.
"""

import math
N = int(input())
res = 0
for j in range(1,N+1):
    for i in range(1,int(math.sqrt(j))+1):
        if j%i == 0 :
            res += i
            if i != j/i :
                res += int(j/i)
print(res)

"""
그래서 각 수의 약수를 구하는 시간 복잡도를 O(N^1/2)로 줄여서
총 O(N^3/2)의 시간 복잡도로 만들었지만, 이 또한 시간초과가 난다.
어떤 수 n의 약수를 구할 때, i가 n의 약수이면 n/i도 약수인 것을 활용한 것이다.
"""

N = int(input())
res = 0
for i in range(1,N+1):
    res += (N//i)*i
print(res)

"""
최종적으로 성공한 코드이다. 시간복잡도를 O(N)까지 줄였다.
약수를 구해서 더하는 것이 아닌, 존재하는 약수들을 더하는 방법으로 해결했다.
말로 하니 이상한데, 예를들어 1~4까지의 약수들을 더할 때,
1을 약수로 가진 것들의 수를 N//1로 구하고, 거기에 약수를 곱해서 res에 더하는 방식을 사용하였다.
2를 약수로 가진 것들의 수는 N//2, 3은 N//3,...이러한 방식이다.
"""
