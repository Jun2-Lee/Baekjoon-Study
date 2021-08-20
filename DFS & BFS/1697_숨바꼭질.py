from collections import deque
n,k = map(int, input().split())
max = 200000                                      # +1 로만 10만까지 갔을때 10만초가 걸리고, 20만에서 -1로만 10만까지 왔을 경우보다 많은 경우는 없기 때문에 20만을 쵀댓값으로 잡아주었다
index = [-1]*max
index[n] = 0
q = deque()
q.append(n)
while q:                                          # BFS의 
    now = q.popleft()
    for next in [now + 1, now - 1, now * 2]:
        if 0 <= next < max and index[next] == -1:
            index[next] = index[now] + 1
            q.append(next)
print(index[k])
