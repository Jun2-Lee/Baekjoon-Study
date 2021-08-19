from collections import deque
n, m, v = map(int,input().split())
d = [[] for _ in range(n+1)]
visit = [False]*(n+1)

for i in range(m):
    node1, node2 = map(int,input().split())     # 받은 입력들을 인접 리스트에 저장한다
    d[node1].append(node2)
    d[node2].append(node1)
for i in range(n+1):
    d[i].sort()                                 # 오름차순 탐색을 위해 정렬해준다

def DFS(node):                                  # DFS 구현 부분이다
    visit[node] = True                          # 먼저, 해당 node를 방문한 것으로 상태를 바꿔준다
    print(node, end = ' ')
    for i in d[node]:                           # 해당 노드에서 갈 수 있는 노드를 찾는다
        if visit[i] == False:                   # 갈 수 있는 노드를 방문한 적 없으면, 방문한 것으로 상태를 바꿔준 뒤 DFS를 재귀호출 한다
            DFS(i)

def BFS(node):                                  # BFS 구현 부분이다
    q = deque()
    q.append(node)                              # node를 큐에 먼저 넣는다
    visit[node] = True                          # 큐에 넣은 노드를 방문한 것으로 상태를 바꿔준다
    while q:
        i = q.popleft()                         # 큐에 있는 첫 번째 인자를 i에 저장하고, i에서 갈 수 있는 노드를 찾은 뒤, 방문한 적이 없으면 다시 큐에 저장하는 것을 반복해준다.
        print(i,end = ' ')
        for j in d[i]:
            if visit[j] == False:
                q.append(j)
                visit[j] = True


DFS(v)
for i in range(n+1):
    visit[i] = False
print()
BFS(v)
