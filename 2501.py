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

