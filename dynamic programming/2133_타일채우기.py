N = int(input())
d = [0]*31
d[0] = 1
d[2] = 3
for i in range(4,31):
    d[i] = d[i-2]*3 # 마지막이 n = 2인 경우로 끝난 경우의 수를 저장해준다.
    for j in range(4,i+1,2):
        d[i] += d[i-j]*2 # 마지막에 n = 4~n까지로 끝난 경우의 수들을 모두 더해준다.
print(d[N])
