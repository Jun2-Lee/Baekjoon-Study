N = int(input())
A = list(map(int,input().split()))
d = [0]*N
num = [-1]*N
max_d = 0
for i in range(N):                  # 11053번에서 풀었던 가장 긴 증가하는 부분수열 part이다.
    d[i] = 1
    for j in range(0,i):
        if A[i] > A[j]:
            if d[i] < d[j]+1:
                d[i] = d[j]+1
                num[i] = j          # 어떤 수에서 왔는지 추적하기 위한 배열을 하나 추가하였다.
    if max_d < d[i]:
        max_d = d[i]
ans = []
for i in range(N):
    if max_d == d[i]:               # 어떤 수에서 끝나는지 찾아서 last_i라는 변수에 저장해주었다.
        last_i = i
for _ in range(max_d):              # 마지막 수에서부터 거꾸로 역추적해서 첫번째 수까지 배열에 저장해주었다.
    ans.append(A[last_i])
    last_i = num[last_i]
ans.reverse()                       # 거꾸로 저장되었기 때문에 reverse 해 주었다.
print(max_d)
print(' '.join(map(str,ans)))
