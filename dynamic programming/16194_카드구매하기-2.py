N = int(input())
P = [0] + list(map(int,input().split()))
d = [10000000]*(N+1) # 최솟값을 구하는 문제이기에 주어진 보기에서의 최댓값으로 초기화해주었다.
d[0] = 0
for i in range(1,N+1):
    for j in range(1,i+1):
        d[i] = min(d[i], d[i-j] + P[j])
print(d[N])
