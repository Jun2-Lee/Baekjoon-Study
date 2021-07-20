while(1):
    try:
        a,b = map(int, input().split())
        print(a+b)
    except:
        break
"""
수를 몇개 입력받을 지 알지 못한 상태에서 try except 구문으로 
입력받지 못하면 break를 걸어준 코드이다
"""
