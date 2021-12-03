from collections import deque

dist = [[-1]*2 for _ in range(500001)]
n, k = map(int, input().split())
q = deque()
q.append((n, 0))
dist[n][0] = 0
while q:
    x, t = q.popleft()
    for y in [x+1, x-1, 2*x]:
        if 0 <= y <= 500000:
            if dist[y][1-t] == -1:
                dist[y][1-t] = dist[x][t] + 1
                q.append((y, 1-t))

ans = -1
t = 0
while True:
    k += t
    if k > 500000:
        break
    if dist[k][t%2] <= t:
        ans = t
        break
    t += 1

print(ans)