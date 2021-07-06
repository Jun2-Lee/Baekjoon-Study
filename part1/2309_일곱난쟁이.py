dworf = []
sum = 0
key = 0
for i in range(9):
    dworf.append(int(input()))
    sum += dworf[i]
for i in range(9):
    if key == 100:
        break
    for j in range(i+1,9):
        key = sum-dworf[j]-dworf[i]
        if (key==100):
            dworf.remove(dworf[j])
            dworf.remove(dworf[i])
            break;
dworf.sort()
for i in range(7):
    print(dworf[i])
    
"""
9명 난쟁이의 키를 입력받고 
이 중 7명의 키 합이 100이 되는 7명을 출력하는 코드이다
"""
