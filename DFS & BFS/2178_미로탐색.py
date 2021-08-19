from collections import deque
n,m = map(int,input().split())
a = [list(map(int,list(input()))) for _ in range(n)]

dx = [0,0,1,-1]                                           # 이동할 수 있는 곳의 좌표
dy = [1,-1,0,0]
visit = [[False]*m for _ in range(n)]
index = [[0]*m for _ in range(n)]                         # 최단거리를 저장하기 위한 배열
q = deque()                                               # '최단' 거리를 구하는 경우에는 DFS가 아닌 BFS를 사용해야 한다. 그 이유는 BFS는 단계별로 방문하기 때문.
q.append((0,0))
visit[0][0] = True                                        # 시작점을 방문했다고 표시해준다
index[0][0] = 1                                           # 시작점의 index는 1
while q:                                                  # BFS의 구현부분. 이동할 수 있는 곳으로 이동한 뒤 index를 1 증가시켜준고, 방문했다고 표시해준다.
    x,y = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if visit[nx][ny] == False and a[nx][ny] == 1:
                q.append((nx,ny))
                index[nx][ny] = index[x][y] + 1
                visit[nx][ny] = True

print(index[n-1][m-1])
