def dfs(node, visited, v):
    global ans, Tree

    if ans[0] < v:
        ans = (v, node)

    for w, c in Tree[node]:
        if not visited[c]:
            visited[c] = True
            dfs(c, visited, v+w)


N = int(input())
Tree = [[] for _ in range(N+1)]
for _ in range(N-1):
    p, c, w = map(int, input().split())
    Tree[p].append((w, c))
    Tree[c].append((w, p))

visited = [False] * (N+1)
visited[1] = True
ans = (0, 1)
dfs(1, visited, 0)
visited = [False] * (N+1)
visited[ans[1]] = True
dfs(ans[1], visited, 0)
print(ans[0])



# 12
# 1 2 3
# 1 3 2
# 2 4 5
# 3 5 11
# 3 6 9
# 4 7 1
# 4 8 7
# 5 9 15
# 5 10 4
# 6 11 6
# 6 12 10