N = int(input())
A = list(map(int,input().split()))
d_up = [0]*N                                          # 배열을 up, down으로 나누어 i로 끝나는 증가하는 수열과, i로 시작하는 감소하는 수열을 저장한다.
d_down = [0]*N
for i in range(N):                                    # i로 끝나는 증가하는 부분수열 part
    d_up[i] = 1
    for j in range(i):
        if A[i] > A[j] and d_up[j] + 1 > d_up[i]:
            d_up[i] = d_up[j] + 1
for i in range(N-1,-1,-1):                            # i로 시작하는 감소하는 부분수열 part
    d_down[i] = 1
    for j in range(i+1, N):
        if A[i] > A[j] and d_down[i] < d_down[j] + 1:
            d_down[i] = d_down[j]+1
max = 0
for i in range(N):                                    # i를 기준으로 증.감이 바뀌는 최댓값 탐색
    if max < d_up[i] + d_down[i]:
        max = d_up[i] + d_down[i]
print(max-1)                                          # i가 2번 포함되었기 때문에 1을 빼준다
