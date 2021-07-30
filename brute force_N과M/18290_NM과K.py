N,M,K = map(int,input().split())
a = [list(map(int,input().split())) for _ in range(N)]
use = [[True]*M for _ in range(N)]
ans = -2147483647
def select(count, sum):
    if count == K:
        global ans
        if ans < sum:
            ans = sum
        return
    for i in range(N):
        for j in range(M):
            if use[i][j] == False:
                continue
            ok = True
            if i-1 >= 0 and use[i-1][j] == False:
                ok = False
            if j-1 >= 0 and use[i][j-1] == False:
                ok = False
            if i+1 < N and use[i+1][j] == False:
                ok = False
            if j+1 < M and use[i][j+1] == False:
                ok = False
            if ok:
                use[i][j] = False
                select(count+1,sum+a[i][j])
                use[i][j] = True
select(0,0)
print(ans)

"""
N*M 배열을 입력받은 후, K개의 칸에 있는 수를 더해 가장 큰 값을 찾는 코드이다.
단, 인접한 칸은 선택할 수 없다.

N과M 문제들과 비슷하지만, 2차원 배열이고, 인접한 칸을 선택할 수 없다는 점이 다르다.
ok라는 bool 변수를 만들고, 인접한 칸이면 선택하지 못하도록 하였다.
"""
