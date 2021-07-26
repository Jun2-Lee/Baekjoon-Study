height = []
add_h = 0
key =0
for i in range(9):
    h = int(input())
    height.append(h)
    add_h += h
for i in range(9):
    if key == 100:
        break
    for j in range(i+1,9):
        key = add_h - height[i] - height[j]
        if key == 100 :
            height.remove(height[j])
            height.remove(height[i])
            break
height.sort()
print(height)
print('\n'.join(map(str,height)))

"""
part1 부분에도 있는 일곱난쟁이 문제이다.
기본적으로 모든 키를 더해놓고(변하지 않는 값이기 때문이다) 두명의 키를 빼는 모든 경우를 거쳐서
그 뺀 값이 100이 되면 그 두개의 값을 빼고 나머지의 값을 정렬 후 출력했다.
"""
