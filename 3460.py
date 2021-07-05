T=int(input())
num=[]
for i in range(T):
    num.append(int(input()))
for i in range(T):
    index = 0
    while num[i] !=0 :
        if num[i]%2==1:
            print(index)
            index += 1
            num[i] = num[i]//2
        else:
            index +=1
            num[i] = num[i]//2
        