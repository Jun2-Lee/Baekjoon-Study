N , S = map(int,input().split())
P = list(map(int,input().split()))
count = 0
for i in range(1, (1<<N)): #가능한 모든 부분수열에 대해
    sum_p = sum(P[k] for k in range(N) if (i & (1<<k)) > 0) # 그 부분수열이 k라는 수를 가지고 있으면 더해줌
    if S == sum_p: # 입력받은 S와 같으면 count 를 1 증가
        count += 1
print(count) 
