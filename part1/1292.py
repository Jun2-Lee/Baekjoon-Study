a,b = map(int,input().split())

list=[]
sum=0
for i in range(1,b+1):
    num=i
    for j in range(0,i):
        list.append(num)
for i in range(a,b+1):
    sum +=list[i-1]
print(sum)
