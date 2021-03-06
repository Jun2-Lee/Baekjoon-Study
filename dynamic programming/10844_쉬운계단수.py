d = [[0]*10 for _ in range(101)]                # 2차원 배열로 index와 마지막에 오는 숫자를 저장해준다
for i in range(1,10):
    d[1][i] = 1                                 # 각각의 index 자리마다 최소값인 1로 초기화 해 준다(단, 0으로 시작하는 경우는 제외한다)
for i in range (2,101):
    for j in range(10):
        if 1<=j<=8:                             # 마지막에 오는 숫자가 1~8인 경우에는 그 숫자의 전,후 경우를 더한 경우가 된다
            d[i][j] = d[i-1][j-1] + d[i-1][j+1]
        elif j == 0:                            # 마지막에 오는 숫자가 0인 경우에는 다음에 1만 올 수 있기 때문에 따로 저장해준다
            d[i][j] = d[i-1][j+1]
        elif j == 9:                            # 9의 경우도 마찬가지이다.
            d[i][j] = d[i-1][j-1]
n = int(input())
print(sum(d[n])%1000000000)
