N = int(input())
a = [list(input()) for _ in range(N)]
ans = 0
def check(a):
    n = len(a)
    res = 0
    for i in range(n):
        count = 1
        for j in range(1,n):
            if a[i][j] == a[i][j-1]:
                count += 1
            else:
                count = 1
            if res < count:
                res = count
        count = 1
        for j in range(1,n):
            if a[j][i] == a[j-1][i]:
                count += 1
            else:
                count = 1
            if res < count:
                res = count
    return res
for i in range(N):
    for j in range(N):
        if j+1 < N:
            a[i][j],a[i][j+1] = a[i][j+1], a[i][j]
            temp = check(a)
            if ans < temp:
                ans = temp
            a[i][j],a[i][j+1] = a[i][j+1], a[i][j]
    for j in range(N):
        if j+1 < N:
            a[j][i],a[j+1][i] = a[j+1][i], a[j][i]
            temp = check(a)
            if ans < temp:
                ans = temp
            a[j][i],a[j+1][i] = a[j+1][i], a[j][i]
print(ans)

"""
사탕의 색이 다른 인접한 두 칸을 고른다. 그 다음 고른 칸에 들어있는 사탕을 서로 교환한다. 
이제, 모두 같은 색으로 이루어져 있는 가장 긴 연속 부분(행 또는 열)을 고른 다음 그 사탕을 모두 먹는다.
사탕이 채워진 상태가 주어졌을 때, 상근이가 먹을 수 있는 사탕의 최대 개수를 구하는 프로그램을 작성하는 문제이다.
사탕의 색이 같은지 확인하는 check를 함수로 구현한 뒤, 사탕의 자리를 하나씩 바꾸고, 제일 긴 줄을 찾는 방식을 사용했다.
모든 자리를 한번씩 바꿔보는 브루트포스 방법이다.
"""
