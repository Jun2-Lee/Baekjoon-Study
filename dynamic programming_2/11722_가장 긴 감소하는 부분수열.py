N = int(input())
A = list(map(int, input().split()))
d = [0]*N
for i in range(N-1, -1, -1):                # i번째에서 시작하는 수열 형식으로 탐색하기 위해 for문을 거꾸로 돌려 주었다.
    d[i] = 1
    for j in range(i+1,N):                  # i보다 뒤에 있으면서 A[i]보다 작은 값이어야 하고, 그 중에 최댓값을 찾기 위해 j를 끝까지 탐색했다.
        if A[i] > A[j] and d[i] < d[j]+1:
            d[i] = d[j] + 1
print(max(d))
