from collections import deque

a, b, c = map(int, input().split())
d = [[[False]*201 for _ in range(201)] for _ in range(201)]

q = deque()
answer = set()
q.append((0, 0, c))
d[0][0][c] = True

while q:
    ca, cb, cc = q.popleft()

    if ca == 0:
        answer.add(cc)

    


# 8 9 10