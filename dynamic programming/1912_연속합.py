n = int(input())
num = list(map(int,input().split()))
d = [0]*n
d[0] = num[0]
for i in range(1,n):
    d[i] = num[i]                     # 초기값으로 그 수 하나만 선택했을 경우를 넣어준다
    if d[i] < d[i-1] + num[i]:        # 그 이전 수열의 최댓값에 현재값을 더한 경우를 비교해주고, 큰 값으로 저장한다.
        d[i] = d[i-1] + num[i]
print(max(d))
