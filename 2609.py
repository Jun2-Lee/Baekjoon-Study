num1,num2 = map(int, input().split())
num1_div = []
num2_div = []
GCM = 0
LCM = 0
for i in range(1,num1+1):
    if num1%i == 0:
        num1_div.append(i)
for i in range(1,num2+1):
    if num2%i == 0:
        num2_div.append(i)
for i in range(len(num1_div)):
    for j in range(len(num2_div)):
        if num1_div[i]==num2_div[j]:
            GCM = num1_div[i]
print(GCM)
LCM = num1*num2//GCM
print(LCM)

"""
GCM을 유클리드 호재법으로 구하는 법
if num1 > num2 :
    large_n = num1
    small_n = num2
c = large_n%small_n
while (c!=0):
    large_n = small_n
    small_n = c
    c = large_n%small_n
GCM = c
이렇게 GCM을 유클리드 호재법으로도 구할 수 있다
    """