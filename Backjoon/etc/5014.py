from collections import deque

F, S, G, U, D = map(int, input().split())
Direction = [U, -D]
dp = [float('inf')]*(F+1)

q = deque()
q.append((S, 0))
dp[S] = 0

ans = -1
while q:
    curr, cnt = q.popleft()
    if curr == G:
        ans = cnt
        break

    for i in Direction:
        nxt = curr + i
        if nxt <= 0 or nxt > F:
            continue
        if dp[nxt] > cnt+1:
            dp[nxt] = cnt+1
            q.append((nxt, cnt+1))

if ans == -1:
    print("use the stairs")
else:
    print(ans)

# 10 1 10 2 1
# 100 2 1 1 0