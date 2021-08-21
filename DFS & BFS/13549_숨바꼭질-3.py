from collections import deque
q = deque()
index = [-1]*200000                             # 이전 숨바꼭질과 동일하게 최댓값을 200000으로 지정해준다
n,k = map(int,input().split())
index[n] = 0
q.append(n)
while q:
    now = q.popleft()
    if now*2 < 200000 and index[2*now] == -1:   # 순간이동을 한 경우 0초가 걸리니까 덱의 앞부분에 추가해준다
        index[2*now] = index[now]
        q.appendleft(2*now)
    if now+1 < 200000 and index[now+1] == -1:   # 순간이동을 한 경우가 아니면 1초가 걸리니까 덱의 뒷부분에 추가해준다
        index[now+1] = index[now] + 1
        q.append(now+1)
    if now-1 >= 0 and index[now-1] == -1:       
        index[now-1] = index[now] + 1
        q.append(now-1)    

print(index[k])
