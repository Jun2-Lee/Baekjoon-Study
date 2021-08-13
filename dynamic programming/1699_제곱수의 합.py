N = int(input())
d = [0]*(N+1)
for i in range(N+1):
    d[i] = i                    # 초기값으로는 1^2 으로만 더해졌을 경우를 저장
    j = 1
    while j*j <= i:             # 제곱수가 찾고자 하는 수를 넘지 않을 때 까지만 탐색
        if d[i] > d[i-j*j]+1:   # 원래 저장되어있는 값보다 새로 찾은 값이 작은경우 최신화
            d[i] = d[i-j*j]+1
        j += 1
print(d[N])
