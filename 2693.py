T=int(input())
answer = []
for i in range(T):
    list_A = list(map(int,input().split()))
    list_A.sort(reverse=True)
    answer.append(list_A[2])
for i in range(T):
    print(answer[i])
    