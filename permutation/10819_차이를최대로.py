N = int(input())
a = list(map(int,input().split()))
a.sort()
ans = -1600

def next_p(p): #10972번에서 작성했던 다음 순열을 구하는 함수
    i = len(p)-1
    while (i>0 and p[i-1]>=p[i]):
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

def sum(a): # 수열 식을 더한 값 구하기
    sum = 0
    for i in range(1,len(a)):
        sum += abs(a[i]-a[i-1])
    return sum

while True: # 다음 수열이 있을 때 까지 반복
    temp = sum(a)
    ans = max(ans,temp)
    if not next_p(a) :
        break

print(ans)
