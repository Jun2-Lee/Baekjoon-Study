N, K = map(int,input().split())
d = [[0]*(N+1) for _ in range(K+1)]
d[0][0] = 1
for i in range(1,K+1):
    for j in range(N+1):
        for k in range(j+1):
            d[i][j] += d[i-1][j-k]
        d[i][j] %= 1000000000
print(d[K][N])
