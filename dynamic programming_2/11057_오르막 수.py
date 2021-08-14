N = int(input())
d = [[0]*10 for _ in range(N+1)]
for i in range(10):
    d[1][i] = 1                     # 숫자가 1개인 경우에는 1가지 경우로 초기화 해 준다.
for i in range(1,N+1):
    for j in range(10):
        for k in range(j+1):
            d[i][j] += d[i-1][k]    # 그 이전 수열의 마지막 수가 현재 수열의 마지막 수와 같아질 때까지 더해준다
            d[i][j] %= 10007        # 메모리를 절약하기 위해 나머지 연산을 해준다.
print(sum(d[N])%10007)
