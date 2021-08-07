N = int(input())
P = [0] + list(map(int,input().split()))
d = [0]*(N+1)
for i in range(1,N+1):
    for j in range(1,i+1):
        d[i] = max(d[i], d[i-j] + P[j])# N장의 카드를 구매하는 경우는 N-?의 카드를 구매한 후, ?짜리 카드를 구매하는 경우이다. 
                                       # 따라서 반복문으로 ?를 1장부터 N장까지 모두 실행시킨 후, 최댓값을 구하였다
print(d[N])
