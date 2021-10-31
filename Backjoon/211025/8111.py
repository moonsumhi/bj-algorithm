# 0과 1로만 이루어져 있어야 한다.
# 1이 적어도 하나 있어야 한다.
# 수의 길이가 100 이하이다.
# 수가 0으로 시작하지 않는다.

from collections import deque
t = int(input())
for _ in range(t):
    n = int(input())
    via = [-1]*n
    how = [-1]*n
    dist = [-1]*n
    q = deque()
    q.append(1%n)
    dist[1%n] = 0
    how[1%n] = 1
    while q:
        now = q.popleft()
        for i in [0,1]:
            next = (now*10+i)%n
            if dist[next] == -1:
                dist[next] = dist[now] + 1
                via[next] = now
                how[next] = i
                q.append(next)
    if dist[0] == -1:
        print('BRAK')
    else:
        ans = ''
        i = 0
        while i != -1:
            ans += str(how[i])
            i = via[i]
        print(ans[::-1])


# 6
# 17
# 11011
# 17
# 999
# 125
# 173