N,M = map(int,input().split())
use = [True]*(N+1)
ans = [0]*M
def num(index,start, N, M):
    if index ==  M:
        print(' '.join(map(str,ans)))
        return
    for i in range(start,N+1):
        if use[i] == False:
            continue
        use[i] = False
        ans[index] = i
        num(index+1,i+1, N, M)
        use[i] = True
num(0,1,N,M)

"""
N과M-1 번 문제와 유사하지만, 다른 점은 수열의 수가 오름차순이어야 한다는 것이다.
이를 해결해주기 위해 함수에 start 매개변수를 하나 더 주어서 다음 index의 수를 정할 때 사용한 숫자보다 1 증가시킨 부분부터 탐색하도록 하였다.
"""
