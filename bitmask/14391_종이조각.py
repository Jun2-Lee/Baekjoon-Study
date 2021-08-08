N, M = map(int,input().split())
a = [list(map(int,list(input()))) for _ in range(N)]
ans = 0
for s in range(1<<(N*M)): # 1<<(N*M) 즉, N*M만큼의 자리수가 1로 가득 채워질 때까지 반복한다.
    sum = 0
    for i in range(N):
        cur = 0
        for j in range(M):
            k = i*M+j # 2차원 배열의 index를 1차원으로 변환
            if(s&(1<<k)) == 0:
                cur = cur*10 + a[i][j] # 가로로 이어져 있는 종이조각이면, 숫자를 이어붙혀준다.
            else:
                sum += cur # 세로로 끊어진 종이조각을 만나면, 이어붙혔던 수를 sum에 더해준다.
                cur = 0
        sum += cur # 마지막이 가로로 끝났을 경우를 위해 한번 더 더해준다.
    for j in range(M): # 세로로 이어진 경우의 조각을 가로와 같은 방법으로 더해준다.
        cur = 0
        for i in range(N):
            k = i*M+j
            if(s&(1<<k)) != 0:
                cur = cur*10 + a[i][j]
            else:
                sum += cur
                cur = 0
        sum += cur
    if ans < sum :
        ans = sum # 최댓값을 저장한다.
print(ans)
