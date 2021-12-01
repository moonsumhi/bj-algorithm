from collections import deque

x, y = map(int, input().split())
q = deque()
q.append((x, y, 0))

while q:
    cur_x, cur_y, t = q.popleft()
    next_t = t + 1
    next_y = cur_y + next_t

    if cur_x == cur_y:
        print(t)
        break

    if next_y < 0 or next_y > 500000:
        continue

    if 0 <= cur_x-1 <= 500000:
        q.append((cur_x-1, next_y, next_t))
    if 0 <= cur_x+1 <= 500000:
        q.append((cur_x+1, next_y, next_t))
    if 0 <= 2*cur_x <= 500000:
        q.append((2*cur_x, next_y, next_t))
else:
    print(-1)

# 5 17