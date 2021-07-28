N,M = map(int,input().split())
ans = [0]*M
def num(index, N, M):
    if index ==  M:
        print(' '.join(map(str,ans)))
        return
    for i in range(1,N+1):
        ans[index] = i
        num(index+1, N, M)
num(0,N,M)

"""
1번 문제와 달라진 점은 숫자 중복 사용이 허가되었다는 것이다.
그렇기 때문에 중복 사용을 막기 위해 선언했던 use 배열을 없애고 수열을 탐색해 주었다.
"""
