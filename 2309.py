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