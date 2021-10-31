import sys
input = sys.stdin.readline
n, k = map(int, input().split())
s = [[] for i in range(n + 1)]
d = [0 for i in range(n + 1)]
def dfs(start):
    if visit[start] == 1:
        return 0
    visit[start] = 1
    print(start)
    print("visit : ", visit)
    for i in s[start]:
        print("i: ", i)
        print(d)
        if d[i] == 0 or dfs(d[i]):
            d[i] = start
            return 1
    return 0
for i in range(k):
    a, b = map(int, input().split())
    s[a].append(b)
print(s)
for i in range(1, n + 1):
    print("--")
    visit = [0 for _ in range(n + 1)]
    dfs(i)
print(d)
print(len(d) - d.count(0))

# 3 5
# 1 1
# 1 3
# 2 2
# 3 2
# 2 3