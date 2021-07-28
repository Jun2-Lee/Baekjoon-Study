N,M = map(int,input().split())
use = [True]*(N+1)
ans = [0]*M
def num(index, N, M):
    if index ==  M:
        print(' '.join(map(str,ans)))
        return
    for i in range(1,N+1):
        if use[i] == False:
            continue
        use[i] = False
        ans[index] = i
        num(index + 1, N, M)
        use[i] = True
num(0,N,M)

"""
자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 코드이다.
1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열

첫 번째 자리를 index 0으로 놓고, 한칸씩 증가시켜가며 재귀 호출로 수열을 채워주었다.
이미 사용한 숫자를 다시 사용하는 것을 피하기 위해 use 배열을 선언, 사용한 숫자를 False로 초기화 해 주었다.
"""
