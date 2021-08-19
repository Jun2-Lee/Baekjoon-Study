n = int(input())
a = [list(map(int,list(input()))) for _ in range(n)]
group = [[0]*n for _ in range(n)]
dx = [0,0,1,-1]                                       # 이동할 수 있는 곳과의 거리를 저장해주었다
dy = [1,-1,0,0]
cnt = 0

def DFS(x,y,cnt):
    group[x][y] = cnt                                 # 해당 노드를 방문했다고 표시
    for i in range(4):                                # 인접한 곳이 4곳이기 때문에 각각 한번씩 탐색
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if a[nx][ny] == 1 and group[nx][ny] == 0: # 이동을 했을 때, 아파트가 있고, 아직 방문하지 않은 곳이면 DFS를 재귀호출해준다
                DFS(nx,ny,cnt)

for i in range(n):                                    # 각각의 연결 요소마다 탐색을 해 주고, 연결요소의 개수를 
    for j in range(n):
        if a[i][j] == 1 and group[i][j] == 0:
            cnt += 1
            DFS(i,j,cnt)
k = 1
print(cnt)  
ans = []    
while k <= cnt:
    num = 0
    for i in range(n):
        for j in range(n):
            if group[i][j] == k:
                num += 1
    ans.append(num)
    k += 1
ans.sort()
print('\n'.join(map(str,ans)))
