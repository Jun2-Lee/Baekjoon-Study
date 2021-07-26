N = int(input())
M = int(input())
remote = [True]*10
if M>0:
    b = list(map(int,input().split()))
for i in range(M):
    remote[b[i]] = False
def check(n):
    if n == 0:
        if remote[n] == True:
            return 1
        else:
            return 0
    len = 0
    while n > 0:
        if remote[n%10] == False :
            return 0
        n = n // 10
        len += 1
    return len
num = abs(N - 100)
for i in range(0,1000001):
    res = check(i)
    if res > 0:
        if res + abs(N-i) < num:
            num = res + abs(N-i)
print(num) 

"""
리모컨에는 버튼이 0부터 9까지 숫자, +와 -가 있다. 
어떤 버튼이 고장났는지 주어졌을 때, 
채널 N으로 이동하기 위해서 버튼을 최소 몇 번 눌러야하는지 구하는 프로그램이다.

처음으로, 리모컨의 어떤 버튼이 고장났는지 저장하기 위한 배열 remote를 만들었다.
그 후, 고장난 버튼을 입력받고 고장이 났으면 False 값을, 고장이 나지 않으면 그대로 True값을 가지게 만들어 주었다.

check함수는 어떤 채널 n을 입력받은 뒤 그 채널의 버튼을 누를 때, 고장난 버튼이 없으면 버튼을 누른 횟수 len을 반환해주고,
고장난 버튼이 있으면 0을 반환하는 함수이다.

구현부에서는 num에 채널 숫자를 누르지 않고 +와 -만으로 채널까지 갔을 경우의 버튼을 누르는 횟수를 저장해주고,
for문에서 1부터 1000000까지의 채널에서 각 채널마다 N까지 가는데 필요한 횟수를 모두 계산, 
그리고 최솟값으로 num을 초기화 시켜주는 것으로 우리가 구하고자 하는 횟수를 구할 수 있다.
"""
