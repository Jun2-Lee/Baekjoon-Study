n,m = map(int,input().split())
d = [[] for _ in range(n+1)]
visit = [False]*(n+1)
for i in range(m):                  # 입력받은 것을 인접 리스트에 저장
    u,v = map(int,input().split())
    d[u].append(v)
    d[v].append(u)

def DFS(node):                      # DFS를 함수로 구현한 부분
    visit[node] = True
    for i in d[node]:
        if visit[i] == False:
            DFS(i)

cnt = 0

for i in range(1,n+1):
    if visit[i] == False:           # 모든 깊이까지 탐색을 했음에도 방문하지 않은 노드가 있을 경우 count를 1 증가시키고 다시 탐색
        DFS(i)
        cnt += 1

print(cnt)
