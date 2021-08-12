N = int(input())
A = list(map(int,input().split()))
d = [0]*N
max_d = 0
for i in range(N):
    d[i] = 1                          # 모든 경우의 초기값을 1로 초기화 해 준다.
    for j in range(0,i):
        if A[i] > A[j]:               # 수열의 수가 증가하고 있고,
            if d[i] < d[j]+1:         # 앞의 부분수열 중에서 가장 길게 이어진 부분수열 뒤에 A[i]를 붙이지만, 우리는 길이만을 필요로 하기 때문에 길이만 바꿔준다
                d[i] = d[j]+1
    if max_d < d[i]:
        max_d = d[i]
print(max_d)
