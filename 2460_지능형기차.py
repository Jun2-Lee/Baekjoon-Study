num = 0
max_num = 0
for i in range(10):
    r_off,r_on = map(int,input().split())
    num = num - r_off + r_on
    if num > max_num:
        max_num = num
print(max_num)
"""
기차에 사람이 최대로 많이 탄 경우의 사람 수를 출력하는 코드이다
"""
