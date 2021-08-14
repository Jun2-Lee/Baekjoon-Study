d = [0]*1000001
d[0] = 1
for i in range(1,1000001):
    if i == 1:                            # 만드는 수가 1인 경우
        d[i] = d[i-1]
    if i == 2:                            # 만드는 수가 2인 경우
        d[i] = d[i-1] + d[i-2]
    else:                                 # 만드는 수가 3이상일 경우
        d[i] = d[i-1] + d[i-2] + d[i-3]
    d[i] %= 1000000009
T = int(input())
for _ in range(T):
    n = int(input())
    print(d[n])
