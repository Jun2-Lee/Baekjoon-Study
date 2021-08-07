n = int(input())
d = [0]*(n+1)
d[0] = 1
d[1] = 1
for i in range(2,n+1):
    d[i] = d[i-1]+d[i-2]*2 # 마지막에 들어갈 수 있는 종류가 1가지 늘었다.
print(d[n]%10007)
