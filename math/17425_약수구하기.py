T=int(input())
max = 1000000
sum = [1]*(max+1)
res = [0]*(max+1)
for i in range(2,max+1):
    j = 1
    while i*j <=max:
        sum[i*j] += i
        j+=1
for i in range(1,max+1):
    res[i] = res[i-1]+sum[i]
ans=[]
for i in range(T):
    N=int(input())
    ans.append(res[N])
print('\n'.join(map(str,ans)))

"""
시간복잡도를 줄이기 위해 1~1,000,000까지 모든 약수의 합들을
배열로 만들어 저장해두고, 그 후에 입력받은 수를 배열에서 찾아와
출력하는 방식을 사용했다.
 약수의 합들을 배열로 만들어 저장할 때, 모든 수는 1을 약수로 가지고 있으니,
 배열을 1로 초기화 해주고, 그 후에 2를 가지고 있는 수들의 위치에는 2를 더하는 식으로
 각 수들의 약수의 합을 구해주었다.
 res 배열을 만들 때는 간단한 점화식을 사용해 주었고, 출력할 때 반복문 안에 print함수를 넣으면
 시간초과가 나게 되어서 배열에 저장해 준 후에 한번에 출력해주었다.
"""
