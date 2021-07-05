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
"""
양의 정수 n이 주어졌을 때, 이를 이진수로 나타냈을 때 1의 위치를 모두 찾는 프로그램이다
"""
