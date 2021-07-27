n, m = map(int,input().split())
a = [list(map(int,input().split())) for _ in range(n)]
ans = 0
for i in range(n):
    for j in range(m):
        if j+3 < m:
            temp = a[i][j] + a[i][j+1] + a[i][j+2] + a[i][j+3]
            if ans < temp: ans = temp

        if i+3 < n:
            temp = a[i][j] + a[i+1][j] + a[i+2][j] + a[i+3][j]
            if ans < temp: ans = temp

        if i+1 < n and j+2 < m:
            temp = a[i][j] + a[i+1][j] + a[i+1][j+1] + a[i+1][j+2]
            if ans < temp: ans = temp

        if i+2 < n and j+1 < m:
            temp = a[i][j] + a[i][j+1] + a[i+1][j] + a[i+2][j]
            if ans < temp: ans = temp

        if i+1 < n and j+2 < m:
            temp = a[i][j] + a[i][j+1] + a[i][j+2] + a[i+1][j+2]
            if ans < temp: ans = temp

        if i+2 < n and j-1 >= 0:
            temp = a[i][j] + a[i+1][j] + a[i+2][j] + a[i+2][j-1]
            if ans < temp: ans = temp

        if i-1 >= 0 and j+2 < m:
            temp = a[i][j] + a[i][j+1] + a[i][j+2] + a[i-1][j+2]
            if ans < temp: ans = temp

        if i+2 < n and j+1 < m:
            temp = a[i][j] + a[i+1][j] + a[i+2][j] + a[i+2][j+1]
            if ans < temp: ans = temp

        if i+1 < n and j+2 < m:
            temp = a[i][j] + a[i][j+1] + a[i][j+2] + a[i+1][j]
            if ans < temp: ans = temp

        if i+2 < n and j+1 < m:
            temp = a[i][j] + a[i][j+1] + a[i+1][j+1] + a[i+2][j+1]
            if ans < temp: ans = temp

        if i+1 < n and j+1 < m:
            temp = a[i][j] + a[i][j+1] + a[i+1][j] + a[i+1][j+1]
            if ans < temp: ans = temp

        if i-1 >= 0 and j+2 < m:
            temp = a[i][j] + a[i][j+1] + a[i-1][j+1] + a[i-1][j+2]
            if ans < temp: ans = temp

        if i+2 < n and j+1 < m:
            temp = a[i][j] + a[i+1][j] + a[i+1][j+1] + a[i+2][j+1]
            if ans < temp: ans = temp

        if i+1 < n and j+2 < m:
            temp = a[i][j] + a[i][j+1] + a[i+1][j+1] + a[i+1][j+2]
            if ans < temp: ans = temp

        if i+2 < n and j-1 >= 0:
            temp = a[i][j] + a[i+1][j] + a[i+1][j-1] + a[i+2][j-1]
            if ans < temp: ans = temp

        if j+2 < m:
            temp = a[i][j] + a[i][j+1] + a[i][j+2]
            if i-1 >= 0:
                temp2 = temp + a[i-1][j+1]
                if ans < temp2: ans = temp2

            if i+1 < n:
                temp2 = temp + a[i+1][j+1]
                if ans < temp2: ans = temp2


        if i+2 < n:
            temp = a[i][j] + a[i+1][j] + a[i+2][j]
            if j+1 < m:
                temp2 = temp + a[i+1][j+1]
                if ans < temp2: ans = temp2

            if j-1 >= 0:
                temp2 = temp + a[i+1][j-1]
                if ans < temp2: ans = temp2
print(ans)

"""
테트로미노 하나를 적절히 놓아서 테트로미노가 놓인 칸에 쓰여 있는 수들의 합을 최대로 하는 프로그램을 작성하는 코드이다.
처음 2차원 배열을 입력받고, 주어진 테트로미노를 회전, 대칭을 시키며 가장 큰 경우를 찾는 것이다.

테트로미노가 그렇게 많은 경우가 있는 것이 아니라서 모든 회전, 대칭을 시킨 19가지의 테트로미노를 2차원 배열에 모두 놓아보는
브루트포스 방법을 사용했다.
"""
