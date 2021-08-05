import sys
M = int(sys.stdin.readline())
n = 20
S = 0
for _ in range(M):
    op, *x = sys.stdin.readline().split()
    if len(x) > 0:
        x = int(x[0]) - 1 # 첫 번째 bit부터 쓰기 위해 1을 빼준다
    if op == 'add': #add 부분 구현
        S = (S | (1<<x))
    elif op == 'remove': #remove 부분 구현
        S = (S & ~(1<<x))
    elif op == 'check': #check 부분 구현
        if (S & (1<<x)) > 0:
            sys.stdout.write('1\n')
        else:
            sys.stdout.write('0\n')
    elif op == 'toggle': #toggle 부분 구현
        S = (S ^(1<<x))
    elif op == 'all': #all 부분 구현
        S = (1<<n) - 1
    elif op == 'empty':#empty 부분 구현
        S = 0
