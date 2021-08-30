n = int(input())
a = [list(input()) for _ in range(n)]
k = int(input())
for _ in range(k):
    no,dir = map(int,input().split())
    no -= 1
    d = [0]*n                                 # N,S극의 조건을 만족하는지를 저장할 배열
    d[no] = dir
    for i in range(no-1, -1, -1):             # 시작하는 톱니바퀴를 기준으로 왼쪽의 극들을 탐색해서, 돌아가는지 아닌지를 판별해준다
        if a[i][2] != a[i+1][6]:
            d[i] = -d[i+1]
        else:
            break
    for i in range(no+1, n):                  # 시작하는 톱니바퀴를 기준으로 오른쪽의 극들을 탐색해서, 돌아가는지 아닌지를 판별한다
        if a[i-1][2] != a[i][6]:
            d[i] = -d[i-1]
        else:
            break
    for i in range(n):
        if d[i] == 0:                         # 톱니바퀴가 돌아가지 않으면, 반복문을 건너뛰어준다
            continue
        if d[i] == 1:                         # 톱니바퀴가 오른쪽으로 돌아가면, 배열을 오른쪽으로 한칸씩 옮겨준다
            temp = a[i][7]
            for j in range(7, 0, -1):
                a[i][j] = a[i][j-1]
            a[i][0] = temp
        elif d[i] == -1:                      # 톱니바퀴가 왼쪽으로 돌아가면, 배열을 왼쪽으로 한칸씩 옮겨준다
            temp = a[i][0]
            for j in range(0, 7):
                a[i][j] = a[i][j+1]
            a[i][7] = temp
ans = 0
for i in range(n):
    if a[i][0] == '1':                        # 12시 방향의 극이 N극인 것을 탐색
        ans += 1
print(ans)
