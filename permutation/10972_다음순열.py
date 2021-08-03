N = int(input())
p = list(map(int,input().split()))
def next_p(p): # C++이나 python에서는 이미 함수로 구현되어 있지만, 실제 작동 원리를 위해 구현해보았다.
    i = len(p)-1
    while (i>0 and p[i-1]>p[i]): # 다음에 바뀔 제일 앞자리의 숫자를 탐색
        i -= 1
    if i <= 0: # 사전상 제일 첫번째 순열이면 -1을 출력
        print(-1)
        return

    j = len(p)-1
    while p[j] <= p[i-1]: # 앞에서 고른 앞자리의 숫자와 교체될 위치의 숫자를 탐색
        j -= 1

    p[i-1] ,p[j] = p[j],p[i-1]

    k = len(p)-1
    while i < k:
        p[i],p[k] = p[k],p[i] # 다음 순열 
        i += 1
        k -= 1
    print(' '.join(map(str,p)))

next_p(p)
