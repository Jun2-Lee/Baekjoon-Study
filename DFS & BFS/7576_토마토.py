from collections import deque                                 # 기본적으로 미로탐색과 비슷한 방법을 사용한다.
m,n = map(int,input().split())
a = [list(map(int,input().split())) for _ in range(n)]
dx = [0,0,1,-1]
dy = [1,-1,0,0]
index = [[-1]*m for _ in range(n)]
q = deque()
for i in range(n):                                            # 시작지점이 정해져 있는 것이 아니기에 시작점을 먼저 찾아준다
    for j in range(m):
        if a[i][j] == 1:
            q.append((i,j))
            index[i][j] = 0
while q:                                                      # BFS의 구현부분이다
    x,y = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if a[nx][ny] == 0 and index[nx][ny] == -1:
                q.append((nx,ny))
                index[nx][ny] = index[x][y] + 1

ans = max([max(row) for row in index])                        # 가능한 모든 토마토가 익었을 때, 최대로 걸린 시간을 ans에 저장해준다
for i in range(n):                                            # 중간에 비어있어 토마토가 익지 못한 경우, ans에 -1을 
    for j in range(m):
        if index[i][j] == -1 and a[i][j] == 0:
            ans = -1
print(ans)
