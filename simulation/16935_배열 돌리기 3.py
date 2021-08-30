n,m,r = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(n)]
op = list(map(int,input().split()))                     # 해야 할 연산을 list의 형태로 저장

def op1(A):                                             # 1번 연산에 해당하는 함수
    n = len(A)
    m = len(A[0])
    B = [[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            B[i][j] = A[n-i-1][j]                       # 상하 반전을 시키기 위해 열을 통째로 치환해주었다
    return B

def op2(A):                                             # 2번 연산에 해당하는 함수
    n = len(A)
    m = len(A[0])
    B = [[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            B[i][j] = A[i][m-1-j]                       # 좌우 반전을 위해 행을 통째로 치환해주었다
    return B

def op3(A):                                             # 3번 연산에 해당하는 함수
    n = len(A)
    m = len(A[0])
    B = [[0]*n for _ in range(m)]                       # 90도만큼 회전하면 가로 세로 길이가 서로 바뀌게 된다
    for i in range(m):
        for j in range(n):
            B[i][j] = A[n-j-1][i]                       # 90도만큼 오른쪽으로 돌리기 위해 2중 포문을 사용했다
    return B
       
def op4(A):                                             # 4번 연산에 해당하는 함수
    n = len(A)
    m = len(A[0])
    B = [[0]*n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            B[i][j] = A[j][m-i-1]
    return B
   
def op5(A):                                             # 5번 연산에 해당하는 함수
    n = len(A)
    m = len(A[0])
    B = [[0]*m for _ in range(n)]
    for i in range(n//2):                               # 먼저 4등분을 하기 위해 가로 세로를 2로 나누어서 반복해준다
        for j in range(m//2):
            B[i][j] = A[i+n//2][j]                      # 나눈 부분들의 위치를 서로 바꾸는 반복문이다
            B[i+n//2][j] = A[i+n//2][j+m//2]
            B[i][j+m//2] = A[i][j]
            B[i+n//2][j+m//2] = A[i][j+m//2]
    return B

def op6(A):                                            # 6번 연산에 해당하는 함수
    n = len(A)
    m = len(A[0])
    B = [[0]*m for _ in range(n)]
    for i in range(n//2):
        for j in range(m//2):
            B[i+n//2][j] = A[i][j]
            B[i][j] = A[i][j+m//2]
            B[i][j+m//2] = A[i+n//2][j+m//2]
            B[i+n//2][j+m//2] = A[i+n//2][j]
    return B

func = [op1, op2, op3, op4, op5, op6]

for i in op:
    A = func[i-1](A)

for i in A:
    print(*i, sep=' ')
