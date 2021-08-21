from collections import deque
dx = [0,0,1,-1]                                           # 이동할 수 있는 칸을 저장
dy = [1,-1,0,0]
q = deque()
m,n = map(int,input().split())
index = [[-1]*m for _ in range(n)]
maze = [list(map(int,list(input()))) for _  in range(n)]
index[0][0] = 0                                           # 초기값 설정
q.append((0,0))
while q:
    x,y = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if index[nx][ny] == -1 and maze[nx][ny] == 0: # 방문한 적 없고, 미로에서 벽이 아닌 부분이면 덱의 앞쪽에 추가해주고, 벽을 부수지 않았으니 index는 그대로 저장해준다
                index[nx][ny] = index[x][y]
                q.appendleft((nx,ny))
            if index[nx][ny] == -1 and maze[nx][ny] == 1: # 미로에서 벽인 부분이면 벽을 부수고, index를 1 증가시켜준 뒤, 덱의 뒤쪽에 추가해준다
                index[nx][ny] = index[x][y] + 1
                q.append((nx,ny))

print(index[n-1][m-1])
