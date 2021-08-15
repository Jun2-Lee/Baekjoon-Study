n = int(input())
a = list(map(int,input().split()))
d1 = [0]*n                          # 앞에서부터 구하는 연속합
d2 = [0]*n                          # 뒤에서부터 구하는 연속합
d1[0] = a[0]
d2[n-1] = a[n-1]
for i in range(1,n):                # i로 끝나는 연속합
    d1[i] = a[i]
    if d1[i] < d1[i-1] + a[i]:
        d1[i] = d1[i-1] + a[i]
for i in range(n-2,-1,-1):          # i로 시작하는 연속합
    d2[i] = a[i]
    if d2[i] < d2[i+1] + a[i]:
        d2[i] = d2[i+1] + a[i]
ans = max(d1)                       # 숫자를 지우지 않았을 경우의 최댓값 저장
for i in range(1,n-1):              # i번째 수를 지웠을 때의 최댓값을 구하는 과정
    if ans < d1[i-1] + d2[i+1]:
        ans = d1[i-1] + d2[i+1]
print(ans)
