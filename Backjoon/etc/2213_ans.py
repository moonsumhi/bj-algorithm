import sys
input = sys.stdin.readline
n = int(input())
w = [0] + list(map(int, input().split()))
s = [[] for i in range(n + 1)]
dp = [[0] * 2 for i in range(n + 1)]
visit = [False for i in range(n + 1)]
num = [[[], []] for i in range(n + 1)]


def dfs(start):
    visit[start] = True
    dp[start][0] = w[start]
    num[start][0].append(start)
    for i in s[start]:
        if not visit[i]:
            dfs(i)
            dp[start][0] += dp[i][1]
            for j in num[i][1]:
                num[start][0].append(j)

            if max(dp[i][1], dp[i][0]) == dp[i][1]:
                dp[start][1] += dp[i][1]
                for k in num[i][1]:
                    num[start][1].append(k)
            else:
                dp[start][1] += dp[i][0]
                for k in num[i][0]:
                    num[start][1].append(k)


for i in range(n - 1):
    a, b = map(int, input().split())
    s[a].append(b)
    s[b].append(a)

dfs(1)

if max(dp[1][0], dp[1][1]) == dp[1][0]:
    print(dp[1][0])
    a = num[1][0]
    a.sort()
    print(*a)
else:
    print(dp[1][1])
    a = num[1][1]
    a.sort()
    print(*a)