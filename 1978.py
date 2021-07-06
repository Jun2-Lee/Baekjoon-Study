N = int(input())
num = list(map(int,input().split()))
prime = 0
for i in range(0,N):
    for j in range(2,num[i]+1):
        if(num[i] == j):
            prime += 1
        elif(num[i]%j == 0):
            break
print(prime)