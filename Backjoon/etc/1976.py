
N = int(input())
M = int(input())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))
plan = list(map(int, input().split()))
plan = list(map(lambda x: x-1, plan))

for i in range(N):
    graph[i][i] = 1

for k in range(N):
    for i in range(N):
        for j in range(N):
            if graph[i][k] and graph[k][j]:
                graph[i][j] = 1

s = plan[0]
if len(plan) == 1:
    print("YES")
else:
    for i in plan[1:]:
        if not graph[s][i]:
            print("NO")
            break
        s = i
    else:
        print("YES")


# 3
# 3
# 0 1 0
# 1 0 1
# 0 1 0
# 1 2 3