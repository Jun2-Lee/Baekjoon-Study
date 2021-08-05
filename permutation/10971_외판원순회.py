N = int(input())
W = [list(map(int,input().split())) for _ in range(N)]
p = []
ans = 2147483647
for i in range(N):
    p.append(i)

def next_p(p): # 다음순열 구하기
    i = len(p)-1
    while (i>0 and p[i-1]>p[i]):
        i -= 1
    if i <= 0:
        return False

    j = len(p)-1
    while p[j] <= p[i-1]:
        j -= 1

    p[i-1] ,p[j] = p[j],p[i-1]

    k = len(p)-1
    while i < k:
        p[i],p[k] = p[k],p[i]
        i += 1
        k -= 1
        
    return True

def check(x,y): #각 마을끼리 갈 수 있는지 확인
    if W[x][y] == 0:
        return False
    return True

def cal(p): #마을끼리 갈 수 있을 때, 그 값을 더하기
    sum = 0
    for i in range(0,N-1):
        if check(p[i],p[i+1]) == False:
            return False
        sum += W[p[i]][p[i+1]]
    return sum
while True: # 끝 마을에서 첫 마을로 돌아올 수 있는지 확인하고, 값을 더해준 후 최솟값 저장(마지막 순열까지 반복)
    if cal(p) != False:
        sum = cal(p)
        if check(p[-1],p[0]):
            sum += W[p[-1]][p[0]]
            ans = min(ans,sum)
    if not next_p(p):
        break

print(ans)
