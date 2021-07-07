N = int(input())
num = list(map(int,input().split()))
add,sub,mul,div = map(int,input().split())
i = 0
res = 0
max_n ,min_n = -1000000000,1000000000
def DFS(i,res,add,sub,mul,div):
    global max_n,min_n
    if(i == N):
        if(max_n < res):
            max_n = res
        if(min_n > res):
            min_n = res
        return
    else:
        if add != 0:
            DFS(i+1,res+num[i],add-1,sub,mul,div)
        if sub != 0:
            DFS(i+1,res-num[i],add,sub-1,mul,div)
        if mul != 0:
            DFS(i+1,res*num[i],add,sub,mul-1,div)
        if div != 0:
            if num[i] < 0 and res > 0:
                DFS(i+1,-(res//-(num[i])),add,sub,mul,div-1)
            elif res < 0 and num[i] > 0:
                DFS(i+1,-(-(res)//num[i]),add,sub,mul,div-1)
            else:
                DFS(i+1,res//num[i],add,sub,mul,div-1)
DFS(1,num[0],add,sub,mul,div)
print(max_n)
print(min_n)

"""
N개의 수와 N-1개의 연산자가 주어졌을 때,
 만들 수 있는 식의 결과가 최대인 것과 최소인 것을 구하는 프로그램을 작성하는 코드이다.
재귀호출을 통해 DFS(깊이우선탐색)을 함수로 구현하였다.
"""
