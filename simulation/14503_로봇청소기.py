n,m = map(int,input().split())
x,y,d = map(int,input().split())
dx = [-1,0,1,0]                                                                 # 로봇청소기가 움직일 수 있는 경로를 북 동 남 서의 순서로 만들어주었다.
dy = [0,1,0,-1]
a = [list(map(int,input().split())) for _ in range(n)]
cnt = 0
while True:                                                                     # 로봇청소기가 동작을 멈출 때까지
    if a[x][y] == 0:                                                            # 로봇청소기가 있는 부분이 청소되지 않았으면 청소해준다
        a[x][y] = 2
    if a[x-1][y] != 0 and a[x+1][y] != 0 and a[x][y-1] != 0 and a[x][y+1] != 0: # 로봇청소기의 사방이 청소되었거나, 벽인 경우를 설정해준다
        if a[x-dx[d]][y-dy[d]] == 1:                                            # 로봇청소기의 뒤쪽이 벽인 경우, 가동을 중지한다
            break
        else:
            x -= dx[d]                                                          # 뒤쪽이 벽이 아닌 경우에는 후진을 한 뒤 다시 탐색한다
            y -= dy[d]
    else:                                                                       # 로봇청소기의 사방이 막히지 않은 경우의 동작부분이다
        d = (d + 3) % 4                                                         # 왼쪽으로 회전한 뒤, 청소가 되어있지 않으면 전진한다
        if a[x+dx[d]][y+dy[d]] == 0:                                            
            x += dx[d]
            y += dy[d]
for i in range(n):
    for j in range(m):
        if a[i][j] == 2:
            cnt += 1 
print(cnt)
