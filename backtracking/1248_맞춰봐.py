import sys # 걸리는 시간을 최소화 하기 위해 sys 라이브러리를 활용했다.
N = int(sys.stdin.readline())
sign = list(sys.stdin.readline())
S = [[0]*N for _ in range(N)] # 0으로 초기화 된 N*N 2차원 배열이다
k = 0
ans = [0]*N
for i in range(N): # 입력받은 부호를 2차원 배열에 입력해준다.
    for j in range(i,N):
        S[i][j] = sign[k]
        k += 1

def check(index): # 수열을 입력받으면 계산하여 2차원 배열의 부호와 비교한 뒤 조건에 맞는지 확인한다.
    sum = 0
    for i in range(index,-1,-1):
        sum += ans[i]
        if S[i][index] == '0':
            if sum != 0:
                return False
        elif S[i][index] == '+':
            if sum <= 0:
                return False
        elif S[i][index] == '-':
            if sum >= 0:
                return False
    return True

def make(index): # 수열을 만드는 함수이다.
    if index == N: # N 길이의 수열이 완성되면 종료한다.
        return True
    if S[index][index] == '0': # index,index의 값이 0이면 그 index의 값은 0이 될 수밖에 없다.(?+? == 0 을 만족하려면 ? == 0이어야 하기 때문.)
        ans[index] = 0
        if check(index) and make(index+1) == True : # index에 0을 저장 한 후의 수열을 check한 뒤 false이면 다음 index를 실행하지 않고 종료한다..
            return True
    if S[index][index] == '+': # index,index의 값이 +면 1~10까지의 수만 들어갈 수 있다.
        for i in range(1,11):
            ans[index] = i
            if  check(index) and make(index+1) == True: # index에 어떤 양수를 저장한 뒤 check를 해서 false면 다음 index를 실행하지 않고 종료한다.
                return True      
    if S[index][index] == '-': # index, index의 값이 -면 -1~-10까지의 수만 들어갈 수 있다.
        for j in range(-10,0):
            ans[index] = j
            if check(index) and make(index+1) == True: # index에 어떤 음수를 저장한 뒤 check를 해서 false면 다음 index를 실행하지 않고 종료한다
                return True
    return False # 모든 index를 했지만, 완성되지 않았을 경우에는 false를 반환한다.

make(0)
sys.stdout.write(' '.join(map(str,ans))) # 만들어진 ans 배열을 출력한다.
