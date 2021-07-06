N,K=input().split()
N=int(N)
K=int(K)
list=[]
count =0
for i in range(N+1):
    if i>0:
        if N%i == 0:
            list.append(i)
            count += 1
if K > count : 
    print(0)
else:
    print(list[K-1])
""" 
N,K를 입력받고 N의 약수들 중 
K번째로 작은 약수를 출력하는 코드이다.
약수를 list에 저장한 뒤 원하는 번호의 약수를 출력할 수 있게 했다
"""
