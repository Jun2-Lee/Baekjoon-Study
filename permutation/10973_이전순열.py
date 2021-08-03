N = int(input()) # 다음 순열 문제와 작동 방식은 동일하지만, 조건과 실행이 반대이다.
p = list(map(int,input().split()))
def prev_p(p):
    i = len(p) - 1
    while i > 0 and p[i-1] < p[i]:
        i -= 1
    if i <= 0:
        print(-1)
        return
    j = len(p) - 1
    while p[j] >= p[i-1]:
        j -= 1
    p[i-1],p[j] = p[j],p[i-1]
    k = len(p) - 1
    while i < k:
        p[i],p[k] = p[k],p[i]
        i += 1
        k -= 1
    print(' '.join(map(str,p)))
    
prev_p(p)
