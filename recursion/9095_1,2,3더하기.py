T = int(input())
def make(sum,n):
    if sum == n:
        return 1
    if sum > n:
        return 0
    ans = 0
    ans += make(sum+1,n)
    ans += make(sum+2,n)
    ans += make(sum+3,n)
    return ans
for _ in range(T):
    N = int(input())
    print(make(0,N))
    
"""
정수 n이 주어졌을 때, n을 1, 2, 3의 합으로 나타내는 방법의 수를 구하는 코드이다.
case가 1,2,3밖에 없기에, 재귀를 3가지 case로 호출해 주었다.

정답인 경우는 sum이 n일 때, 불가능한 경우는 sum이 n을 넘어갔을 경우이기 때문에 n이면 1, 불가능하면 0을 return해 주어서
ans에 추가를 해 주었다.
총 시간복잡도는 O(3^N)이다.
"""
