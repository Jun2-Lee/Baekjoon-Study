N,M = map(int,input().split())
num = list(map(int,input().split()))
num.sort()
ans = [0]*M
def check(index,N,M):
    if index == M :
        print(' '.join(map(str,ans)))
        return
    for i in range(N):
        ans[index] = num[i]
        check(index+1,N,M)
check(0,N,M)

"""
15651과 동일한 문제이다.
"""
