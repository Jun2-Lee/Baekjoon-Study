n = int(input())
t = [list(map(int,input().split())) for _ in range(n)]
d = [[0]*n for _ in range(n)]
d[0][0] = t[0][0]                                       # 초기값은 삼각형의 맨 위의 값으로 해준다.
for i in range(1, n):
    for j in range(i+1):
        if j == 0:                                      # 가장 왼쪽의 수는 오른쪽 위의 수에서밖에 올 수 없다.
            d[i][j] = d[i-1][j] + t[i][j]
        if j == i:                                      # 가장 오른쪽의 수는 왼쪽 위의 수에서밖에 올 수 없다.
            d[i][j] = d[i-1][j-1] + t[i][j]
        d[i][j] = max(d[i-1][j-1],d[i-1][j]) + t[i][j]  # 중간의 수들은 왼쪽 위나 오른쪽 위의 수에서 올 수 있다.
print(max(d[n-1]))
