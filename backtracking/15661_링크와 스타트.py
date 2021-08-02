n = int(input())
S = [list(map(int,input().split())) for _ in range(n)]
def make(index, first, second):
    if index == n:
        if len(first) < 1: # 한 팀의 사람 수가 1이 되지 않으면 -1 반환
            return -1
        if len(second) < 1:
            return -1
        t1 = 0
        t2 = 0
        for i in range(len(first)): # 양 팀의 점수를 더함
            for j in range(len(first)):
                t1 += S[first[i]][first[j]]
        for i in range(len(second)):
            for j in range(len(second)):
                t2 += S[second[i]][second[j]]
        temp = abs(t1-t2)
        return temp
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
