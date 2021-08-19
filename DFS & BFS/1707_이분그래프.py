import sys
sys.setrecursionlimit(1000000)                      # 파이썬에서는 재귀함수가 default로 1000까지밖에 실행되지 않아서 제한을 늘려주었다
T = int(sys.stdin.readline())
for _ in range(T):
    V,E = map(int,sys.stdin.readline().split())     # 입력을 인접 리스트에 저장하는 부분
    node = [[] for _ in range(V+1)]
    color = [0]*(V+1)
    for i in range(E):
        u,v = map(int,sys.stdin.readline().split())
        node[u].append(v)
        node[v].append(u)

    def DFS(n,c):                                   # DFS 함수 구현부분
        color[n] = c                                # 방문을 한 것으로 상태를 변경
        for i in node[n]:
            if color[i] == 0:
                if DFS(i,3-c) == False:             # color를 1과 2로 나누어서 구분하였다. 
                    return False
            if color[n] == color[i]:                # 갈 수 있는 노드와 현재 노드가 색이 같으면 false를 반환해준다
                return False
        return True

    ans = True
    for i in range(1,V+1):
        if color[i] == 0:
            if not DFS(i, 1):
                ans = False
    print('YES' if ans else 'NO')
