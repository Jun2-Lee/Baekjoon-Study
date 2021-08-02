k = int(input())
k_list = input().split()
use = [True]*10
ans = []
def check(num1,num2,op): # 부등호에 맞게 숫자가 들어 왔는지 확인하는 함수
    if op == '<':
        if num1 > num2:
            return False
    if op == '>':
        if num1 < num2:
            return False
    return True
def make(index, num):
    if index == k+1: # 부등호의 갯수 +1 만큼의 숫자를 확인
        ans.append(num)
        return
    for i in range(10): # 모든 숫자를 대입해서 확인
        if use[i] == False: # i가 이미 쓰인 숫자면 continue
            continue
        if index == 0 or check(num[index-1],str(i),k_list[index-1]): # 부등호에 맞게 숫자가 들어갔을 경우만 재귀로 다음 index를 탐색함
            use[i] = False
            make(index+1, num + str(i))
            use[i] = True
make(0,'')
ans.sort()
print(ans[len(ans)-1])
print(ans[0])
