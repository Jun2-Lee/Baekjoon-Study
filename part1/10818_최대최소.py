N=int(input())
num =  list(map(int,input().split()))
num.sort()
print(num[0], num[N-1])
"""
수를N개 입력받고 최댓값과 최솟값을 출력하는 코드이다
"""
