import sys
input = sys.stdin.readline
n = int(input())
queue = [0]*n
begin = 0
end = 0
for _ in range(n):
    cmd, *val = input().split()
    if cmd == 'push':
        num = int(val[0])
        queue[end] = num
        end += 1
    elif cmd == 'front':
        if begin == end:
            print(-1)
        else:
            print(queue[begin])
    elif cmd == 'size':
        print(end-begin)
    elif cmd == 'empty':
        if begin == end:
            print(1)
        else:
            print(0)
    elif cmd == 'pop':
        if begin == end:
            print(-1)
        else:
            print(queue[begin])
            begin += 1
    elif cmd == 'back':
        if begin == end:
            print(-1)
        else:
            print(queue[end-1])

# 큐를 직접 코드로 구현해보았다. python에서는 collections.deque라는 라이브러리로 사용할 수 있다.
