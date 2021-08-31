def road(line,l):                                         # 길을 통과할 수 있는지 아닌지를 판별하는 함수아더
    n = len(line)
    check = [False]*n
    for i in range(1,n):
        if line[i] != line[i-1]:                          # 높이가 다른 경우에, 그 높이의 차이가 1이 아니면 경사로를 놓을 수 없기때문에 바로 False를 return 해 준다
            diff = abs(line[i]-line[i-1])
            if diff != 1:
                return False
            if line[i] > line[i-1]:                       # 오른쪽이 더 높게 1 차이 나는 경우, 왼쪽 방향으로 경사로를 놓아야 한다
                for j in range(1,l+1):
                    if i-j < 0:
                        return False
                    if line[i-1] != line[i-j]:
                        return False
                    if check[i-j] == True:
                        return False
                    check[i-j] = True
            if line[i-1] > line[i]:                       # 왼쪽이 더 높게 1 차이 나는 경우, 오른쪽 방향으로 경사로를 놓아야 한다
                for j in range(l):
                    if i+j >= n:
                        return False
                    if line[i] != line[i+j]:
                        return False
                    if check[i+j]:
                        return False
                    check[i+j] = True
    return True

n,l = map(int,input().split())
a = [list(map(int,input().split())) for _ in range(n)]
ans = 0
for i in range(n):                                        # 열 방향 탐색
    line = a[i]
    if road(line,l) == True:
        ans += 1
for j in range(n):                                        # 행 방향 탐색
    line = [a[i][j] for i in range(n)]
    if road(line,l):
        ans += 1
print(ans)
