def next_p(p): # 다음 순열 구하기
    i = len(p)-1
    while (i>0 and p[i-1] >= p[i]):
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

while True: # 순열이 끝날 때까지 반복
    K,*S = list(map(int,input().split()))
    if K == 0 :
        break
    p = [1]*(K-6) + [0]*6 # 로또 번호로 쓸 숫자는 1, 아닌 숫자는 0으로 정해준 뒤, 첫 번째 수열 작성
    p.sort()
    S.sort()
    while True: # 0 위치에 있는 수를 temp 변수에 저장 후, 출력(마지막 수열까지 반복)
        temp = []
        for i in range(K):
            if p[i] == 0:
                temp.append(S[i])
        print(' '.join(map(str,temp)))     
        if not next_p(p):
            break
    print()
