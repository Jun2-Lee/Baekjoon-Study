from collections import deque
T = int(input())
dx = [1,2,2,1,-1,-2,-2,-1]                            # 나이트가 이동할 수 있는 점들을 저장
dy = [2,1,-1,-2,-2,-1,1,2]
for _ in range(T):
    l = int(input())
    index = [[-1]*l for _ in range(l)]                # l * l크기의 체스판 생성
    s_x,s_y = map(int,input().split())
    d_x,d_y = map(int,input().split())
    index[s_x][s_y] = 0                               # 초기값의 index를 0으로 초기화

    q = deque()
    q.append((s_x,s_y))
    while q:                                          # BFS의 구현부분
        x,y = q.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < l and 0 <= ny < l:
                if index[nx][ny] == -1:
                    index[nx][ny] = index[x][y] + 1
                    q.append((nx,ny))
    print(index[d_x][d_y])
