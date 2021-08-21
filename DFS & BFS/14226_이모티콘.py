from collections import deque
n = int(input())
index = [[-1]*2000 for _ in range(2000)]    # 이모티콘과 클립보드를 저장하는 2차원 배열을 만들어줌
q = deque()
q.append((1,0))                             # 초기값 설정
index[1][0] = 0
while q:
    s,c = q.popleft()
    if index[s][s] == -1:                   # 클립보드에 저장을 한 경우
        index[s][s] = index[s][c] + 1
        q.append((s,s))
    if s+c < 2000 and index[s+c][c] == -1:  # 클립보드에 저장한 것을 붙여넣기 한 경우
        index[s+c][c] = index[s][c] + 1
        q.append((s+c,c))
    if index[s-1][c] == -1 and s-1 >= 0:    # 이모티콘을 하나 지운 경우
        index[s-1][c] = index[s][c] + 1
        q.append((s-1,c))
ans = -1
for i in range(2000):                       # 최솟값 
    if index[n][i] != -1:
        if ans == -1 or ans > index[n][i]:
            ans = index[n][i]

print(ans)
