N = int(input())
T = []
P = []
max_p = 0
for i in range(N):
    t, p = map(int,input().split())
    T.append(t)
    P.append(p)
def Pay(day,pay,N):
    global max_p
    if day == N:
        if max_p < pay:
            max_p = pay
        return
    if day > N:
        return
    Pay(day+T[day],pay+P[day],N)
    Pay(day+1,pay,N)
Pay(0,0,N)
print(max_p)

"""
상담할 때 걸리는 시간 T_i와 받는 금액 P_i를 각각 배열로 입력받고,
그 날짜에 해당하는 상담을 하는 경우와 하지 않는 경우로 나누어서 재귀 호출을 하였다.
"""
