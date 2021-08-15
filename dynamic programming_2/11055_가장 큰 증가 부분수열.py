N = int(input())
A = list(map(int, input().split()))
d = [0]*N
for i in range(N):
    d[i] = A[i]
    for j in range(i):
        if A[j] < A[i] and d[j]+A[i] > d[i]:  # 가장 긴 증가하는 부분수열과 다르게 길이가 아닌 수의 크기를 더한 후 비교해준다.
            d[i] = d[j]+A[i]                 
print(max(d))
