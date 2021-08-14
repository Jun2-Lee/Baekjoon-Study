n = int(input())
d = [[0]*3 for _ in range(n+1)]                               # 0 = R, 1 = G, 2 = B로 선택
ans = [0]*(n+1)
for i in range(1,n+1):
    d[i][0],d[i][1],d[i][2] = map(int,input().split()) 
for i in range(1,n+1):
    d[i][0] = min(d[i-1][1] + d[i][0], d[i-1][2] + d[i][0])   # 마지막으로 R을 칠했을 때의 최솟값
    d[i][1] = min(d[i-1][0] + d[i][1], d[i-1][2] + d[i][1])   # 마지막으로 G를 칠했을 때의 최솟값
    d[i][2] = min(d[i-1][0] + d[i][2], d[i-1][1] + d[i][2])   # 마지막으로 B를 칠했을 때의 최솟값
    ans[i] = min(d[i][1],d[i][0],d[i][2])                     # 어떤 색을 칠했을 때 최솟값
print(ans[n])
