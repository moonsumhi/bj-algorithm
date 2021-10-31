from collections import deque


def d(n):
    return int(2 * n % 10000)

def s(n):
    return int((n + 9999) % 10000)

def l(n):
    return int((n * 10) % 10000 + (n/1000))

def r(n):
    return int(n / 10 + (n % 10) * 1000)


def bfs(x, target):

    global ORDER

    q = deque()
    q.append(x)

    dp = ["" for _ in range(10000)]
    while q:
        curr = q.popleft()
        # print("curr, state: ", curr, dp[curr])

        if dp[target]:
            print(dp[target])
            return

        D, S, L, R = d(curr), s(curr), l(curr), r(curr)
        # print(D, S, L, R)
        for idx, v in enumerate([D, S, L, R]):
            if (not dp[v]) and (v != x):
                dp[v] = dp[curr] + ORDER[idx]
                q.append(v)


T = int(input())
ORDER = ["D", "S", "L", "R"]
for _ in range(T):
    a, b = map(int, input().split())
    bfs(a, b)



# 3
# 1234 3412
# 1000 1
# 1 16