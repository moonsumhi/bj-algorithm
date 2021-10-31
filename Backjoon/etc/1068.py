def dfs(node):
    global ans

    if not children[node]:
        ans += 1
        return

    for i in children[node]:
        dfs(i)

def find_parent(node):
    if parents[node] != -1:
        return find_parent(parents[node])
    return node

N = int(input())
parents = list(map(int, input().split()))
rm_node = int(input())
ans = 0
children = [[] for _ in range(N)]

for i in range(N):
    if parents[i] != -1:
        children[parents[i]].append(i)

if parents[rm_node] != -1:
    children[parents[rm_node]].remove(rm_node)
    p = find_parent(parents[rm_node])
    dfs(p)
    print(ans)
else:
    print(0)

# 5
# -1 0 0 1 1
# 2

# 5
# 1 2 3 4 -1
# 4

# 4
# -1 0 1 2
# 2