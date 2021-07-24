def GCD(a,b):
    if b == 0 :
        return a
    else:
        return GCD(b,a%b)
a,b = map(int,input().split())
gcd = GCD(a,b)
print(gcd)
print(a*b//gcd)

"""
GCD라는 함수를 만든 뒤 유클리드 호재법을 이용해
최대공약수를 구했다.
이후 a*b/GCD를 이용해 최소공배수까지 출력하였다
"""
