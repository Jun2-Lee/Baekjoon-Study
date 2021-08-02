n = int(input())
S = [list(map(int, input().split())) for _ in range(n)]
def make(index, first, second):
    if index == n: # 양 팀의 수가 같지 않으면 -1을 반환
        if len(first) != n/2: 
            return -1
        if len(second) != n/2:
            return -1
        sum_f = 0
        sum_s = 0
        for i in range(n//2): # 양 팀의 점수 더하기
            for j in range(n//2):
                sum_f += S[first[i]][first[j]]
                sum_s += S[second[i]][second[j]]
        temp = abs(sum_f-sum_s)
        return temp
    if len(first)>n//2: # 양팀의 수가 같아질 수 없게 되면 더이상 재귀호출을 하지 않음
        return -1
    if len(second)>n//2:
        return -1
    ans = -1
    t1 = make(index+1,first+[index],second)
    if ans == -1 or (t1!=-1 and ans>t1):
        ans = t1
    t2 = make(index+1,first,second+[index])
    if ans == -1 or (t2!=-1 and ans>t2):
        ans = t2   
    return ans
ans = make(0,[],[])
print(ans)
