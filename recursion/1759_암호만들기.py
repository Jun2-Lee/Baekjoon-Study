L, C = map(int, input().split())
alpa = list(map(str,input().split()))
alpa.sort()
def check(pw):
    m = 0
    j = 0
    for i in range(L):
        if pw[i] in 'aeiou':
            m += 1
        else:
            j += 1
    if m>=1 and j>=2:
        return True
    else:
        return False

def make(length, pw, index):
    if len(pw) == length:
        if check(pw) == True:
            print(pw)
        return
    if index == len(alpa):
        return
    make(length, pw+alpa[index], index+1)
    make(length, pw, index+1)
make(L,"",0)

"""
암호는 서로 다른 L개의 알파벳 소문자들로 구성되며 
최소 한 개의 모음(a, e, i, o, u)과 최소 두 개의 자음으로 구성되어 있다
알파벳이 암호에서 증가하는 순서로 배열된다.
C개의 문자들이 모두 주어졌을 때,위의 조건을 만족하는 암호들을 모두 구하는 코드이다.

입력받은 알파벳들을 배열로 받은 뒤, 다음 index의 알파벳을 선택하는 경우, 선택하지 않는 경우로 나누었다.
그렇게 만든 암호들을 check 함수로 모음, 자음 조건을 만족하는지 확인한 후, 만족하면 출력해주었다.
총 시간 복잡도는 O(2^N*L)이다.
"""
