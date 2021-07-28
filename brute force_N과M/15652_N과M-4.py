N,M = map(int,input().split())
ans = [0]*M
def num(index,start, N, M):
    if index ==  M:
        print(' '.join(map(str,ans)))
        return
    for i in range(start,N+1):
        ans[index] = i
        num(index+1,i, N, M)
num(0,1,N,M)

"""
3번과 달라진 점은 2번처럼 수가 내림차순이 아니어야 한다는 것이다.
오름차순이라고 쓰이지 않은 이유는 중복을 허가했기 때문이다.
2번과 마찬가지로 start 매개변수를 하나 더 선언해주고, start부터 수열의 수를 탐색해 주었다.
"""
