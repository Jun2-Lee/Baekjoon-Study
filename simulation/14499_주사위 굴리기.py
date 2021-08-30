dx = [0,0,-1,1]                                         # 주사위가 동 서 남 북으로이동할 때의 좌표를 list로 선언해주었다
dy = [1,-1,0,0]
n,m,x,y,l = map(int,input().split())
a = [list(map(int,input().split())) for _ in range(n)]
dice = [0]*7                                            # 주사위의 면에 적혀있는 수를 적을 배열을 선언해준다
move = list(map(int,input().split()))
for k in move:
    k -= 1
    nx,ny = x+dx[k],y+dy[k]
    if nx < 0 or nx >= n or ny < 0 or ny >= m:          # 주사위가 움직였을 때, 판을 벗어나지 않는가를 조사한다
        continue
    if k == 0:                                          # 주사위가 동쪽으로 움직인 경우에서 면에 적혀있는 값이 변한 부분을 변경해주었다
        temp = dice[1]
        dice[1] = dice[4]
        dice[4] = dice[6]
        dice[6] = dice[3]
        dice[3] = temp
    elif k == 1:                                        # 주사위가 서쪽으로 움직인 경우에서 면에 적혀있는 값이 변한 부분을 변경해주었다 
        temp = dice[1]
        dice[1] = dice[3]
        dice[3] = dice[6]
        dice[6] = dice[4]
        dice[4] = temp
    elif k == 2:                                        # 주사위가 남쪽으로 움직인 경우에서 면에 적혀있는 값이 변한 부분을 변경해주었다
        temp = dice[1]
        dice[1] = dice[5]
        dice[5] = dice[6]
        dice[6] = dice[2]
        dice[2] = temp
    else:                                               # 주사위가 동쪽으로 움직인 경우에서 면에 적혀있는 값이 변한 부분을 변경해주었다
        temp = dice[1]
        dice[1] = dice[2]
        dice[2] = dice[6]
        dice[6] = dice[5]
        dice[5] = temp
    x,y = nx,ny
    if a[x][y] == 0:                                    # 주사위가 이동한 후, 도착한 칸이 0이면 바닥에 주사위의 밑면을 붙여넣어준다
        a[x][y] = dice[6]
    else:                                               # 0이 아니면, 바닥의 숫자를 주사위의 밑면에 복사해주고, 그 칸을 0으로 만든다
        dice[6] = a[x][y]
        a[x][y] = 0
    print(dice[1])                                      # 이동 할 때마다 주사위의 윗면을                  
