N = int(input())
first_p = [] 
for i in range(1,N+1): # 첫번째 순열을 생성
    first_p.append(i)

def next_p(p): # 다음 순열을 만들어주는 함수
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
    return p

print(' '.join(map(str,first_p))) # 첫번째 순열 출력
while next_p(first_p) != False: # 마지막 순열이 아닐때까지 실행
    print(' '.join(map(str,first_p))) 
