N = int(input())
ans = [0]*(N+1) # 각 숫자마다의 최솟값을 저장할 배열
for i in range(2,N+1): 
    ans[i] = ans[i-1] + 1 # 1을 빼는 경우는 다른 조건이 필요 없으니 초기 값으로 저장해줌
    if i%2 == 0 and ans[i] > ans[i//2] + 1: # 2로 나누고, 1을 뺀 경우보다 작으면 저장
        ans[i] = ans[i//2] + 1
    if i%3 == 0 and ans[i] > ans[i//3] + 1: # 3으로 나누고, 1을 뺀 경우나 2로 나눈 경우보다 작으면 저장
        ans[i] = ans[i//3] + 1
print(ans[N])
