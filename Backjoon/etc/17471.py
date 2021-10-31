from itertools import combinations
from collections import deque

def bfs(part):
    global graph

    q = deque()
    q.append(part[0])

    visited = [False]*(N+1)
    visited[part[0]] =True
    while q:
        x = q.popleft()

        for y in graph[x]:
            if visited[y]:
                continue
            if y in part:
                visited[y] = True
                q.append(y)

    if sum(visited) == len(part):
        return True
    else:
        return False


def isPromising(x):
    global nodes

    p1 = set(x)
    p2 = nodes-p1
    p1, p2 = list(p1), list(p2)

    if (not p1) or (not p2):
        return False

    if bfs(p1) and bfs(p2):
        return True

    return False


N = int(input())
nodes = set(i for i in range(1, N+1))
population = [0] + list(map(int, input().split()))
graph = [[] for _ in range(N+1)]
for i in range(1, N+1):
    tmp = list(map(int, input().split()))
    cnt, adj = tmp[0], tmp[1:]
    for j in adj:
        graph[i].append(j)
print(graph)

candi = []
for i in range(1, (N//2) + 1):
    candi += list(combinations(range(1, N+1), i))
print(candi)

diff = float('inf')
for part1 in candi:
    if isPromising(part1):
        population1 = 0
        for e in part1:
            population1 += population[e]
        population2 = sum(population) - population1
        print("part1: ", part1)
        diff = min(diff, abs(population1-population2))
        print("diff: ", diff)

if diff == float('inf'):
    print(-1)
else:
    print(diff)












# 6
# 5 2 3 4 1 2
# 2 2 4
# 4 1 3 6 5
# 2 4 2
# 2 1 3
# 1 2
# 1 2