while True: # K가 0이 입력될 때까지 반복
    K, *S = list(map(int,input().split())) # 숫자들이 입력되면 첫 번째 숫자는 K에, 그 뒤의 숫자들은 S에 list로 입력해줌
    if K == 0:
        break
    S.sort()
    num = []
    def make(index,num,i):
        if i == 6: #고른 숫자가 6개가 되면 출력 후 탈출
            print(' '.join(map(str,num)))
            return
        if index == K: # 숫자를 6개 고르지 못했는데 모든 탐색을 했으면, 실패한 것이니 반환
            return
        make(index+1,num+[S[index]],i+1) # index번째 수를 선택한 경우의 다음 재귀호출
        make(index+1,num,i) # index번째 수를 선택하지 않은 경우의 다음 재귀호출
    make(0,num,0)
    print() # 줄 바꾸기
