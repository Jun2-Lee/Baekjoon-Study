import sys
n, m = map(int,sys.stdin.readline().split())
edges = []
a = [[False]*n for _ in range(n)]
g = [[] for _ in range(n)]
for _ in range(m):                                                    # 입력받은 간선들을 각각 인접 행렬, 인접 리스트, 간선리스트에 저장해주었다.
    u, v = map(int,sys.stdin.readline().split())
    edges.append((u,v))
    edges.append((v,u))
    a[u][v] = a[v][u] = True
    g[u].append(v)
    g[v].append(u)
m *= 2

for i in range(m):                                                    
    for j in range(m):
        A, B = edges[i]                                               # A, B를 잇는 간선을 찾는다(간선 리스트 사용)
        C, D = edges[j]                                               # C, D를 잇는 간선을 찾는다
        if A == B or A == C or A == D or B == C or B == D or C == D:  
            continue
        if not a[B][C]:                                               # 인접 행렬을 사용해서 B와 C를 잇는 간선이 있는지 찾는다
            continue
        for E in g[D]:                                                # 인접 리스트를 사용해서 D와 E를 잇는 간선이 있는지 찾는다.
            if A == E or B == E or C == E or D == E:
                continue
            print(1)                                                  # 모든 것을 찾을 수 있었으면 1을 출력하고 종료한다.
            sys.exit(0)
print(0)
