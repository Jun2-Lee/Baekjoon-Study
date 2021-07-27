N = int(input())
add = 0
start = 1
l = 1
while True:
    end = start* 10 - 1
    if end > N:
        end = N
    add += l * (end-start+1)
    start *= 10
    l += 1
    if end == N:
        break
print(add)

"""
N이라는 수를 입력받으면 1부터 N까지의 모든 수를 이어붙인 뒤 그 길이가 얼마인지 찾는 코드이다.

수를 전부 이어붙이는 연산을 한다면 시간이 너무 오래 걸리기에 1~9까지는 길이가 1씩 증가하고, 10~99까지는 2, 100~999까지는 3,...
이런식으로 자리 수에 따라 길이만 더해주는 연산을 하였다.
"""
