N, M = map(int,input().split())
num = list(map(int,input().split()))
num.sort()
use = [True]*(N+1)
ans = [0]*M
def check(index,start,N,M):
    if index == M:
        print(' '.join(map(str,ans)))
        return
    for i in range(start,N):
        if use[i] == False:
            continue
        use[i] = False
        ans[index] = num[i]
        check(index+1,i+1,N,M)
        use[i] = True
check(0,0,N,M)    

"""
15650과 비슷한 문제이다.
"""
