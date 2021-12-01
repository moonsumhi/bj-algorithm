from collections import deque

a, b = map(int, input().split())
q = deque()
q.append((a, 0))

while q:
    x, cnt = q.popleft()
    print(x)
    if x == b:
        print(cnt+1)
        break

    if 2*x <= b:
        q.append((2*x, cnt+1))

    temp = int(str(x) + "1")
    if temp <= b:
        q.append((temp, cnt+1))
else:
    print(-1)




# 2 162