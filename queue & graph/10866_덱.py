import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
d = deque()

for _ in range(n):
    s = input().split()
    cmd = s[0]
    if cmd == 'push_front':
        num = int(s[1])
        d.appendleft(num)
    elif cmd == 'push_back':
        num = int(s[1])
        d.append(num)
    elif cmd == 'pop_front':
        if d:
            print(d.popleft())
        else:
            print(-1)
    elif cmd == 'pop_back':
        if d:
            print(d.pop())
        else:
            print(-1)
    elif cmd == 'size':
        print(len(d))
    elif cmd == 'empty':
        print(0 if d else 1)
    elif cmd == 'front':
        if d:
            print(d[0])
        else:
            print(-1)
    elif cmd == 'back':
        if d:
            print(d[-1])
        else:
            print(-1)

# 덱을 직접 구현한 코드이다. python에서는 collections.deque라는 라이브러리로 사용할 수 있다.
