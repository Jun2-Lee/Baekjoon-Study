M = int(input())
N = int(input())
sum = 0
min = N
for i in range(M,N+1):
    for j in range(2,i+1):
        if(i == j):
            sum += j
            if(min > j):
                min = j
        elif (i%j == 0):
            break
        
if(sum == 0):
    print(-1)
else:
    print(sum)
    print(min)

