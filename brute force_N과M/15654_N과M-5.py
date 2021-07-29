N, M = map(int, input().split())
num = list(map(int,input().split()))
use = [True]*N
ans = [0] * M
num.sort()
def check(index,N,M):
    if index == M:
        print(' '.join(map(str,ans)))
        return
    for i in range(N):
        if use[i] == False:
            continue
        use[i] = False
        ans[index] = num[i]
        check(index+1,N,M)
        use[i] = True
        
check(0,N,M)

"""
15649번과 거의 동일한 문제지만, 수열을 구성하는 수를 직접 입력해준다는 점이 다르다.
따라서 num배열을 만들고 수를 입력받은 뒤, i를 이용해서 수열을 탐색하였다.
"""
