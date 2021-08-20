from collections import deque
import sys                                          # 재귀 호출의 횟수를 늘려주기 위해 사용
sys.setrecursionlimit(10000000)
n,k = map(int, input().split())
max = 200000
index = [-1]*max
index[n] = 0
pre = [-1]*max                                      # 이동경로를 저장하기 위한 배열
q = deque()
q.append(n) 
while q:                                            # BFS의 구현부분
    now = q.popleft() 
    for next in [now + 1, now - 1, now * 2]:        
        if 0 <= next < max and index[next] == -1:
            index[next] = index[now] + 1      
            pre[next] = now                         # 이동경로를 저장
            q.append(next)
print(index[k])

def out(n,k):                                       # 이동경로를 역추적해 출력하는 
    if n != k:
        out(n,pre[k])
    print(k,end = ' ')
out(n,k)
