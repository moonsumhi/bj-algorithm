import copy


def print_graph(g):
    print("=============")
    for i in g:
        print(i)


def dfs(x, y, g):
    global D, visited
    cur_color = g[x][y]
    for i, j in D:
        n_x, n_y = x+i, y+j
        if n_x < 0 or n_y < 0 or n_x >= N or n_y >= N:
            continue
        if visited[n_x][n_y]:
            continue
        if g[n_x][n_y] == cur_color:
            visited[n_x][n_y] = True
            dfs(n_x, n_y, g)


N = int(input())
graph = []
for _ in range(N):
    graph.append(list(input()))

ngraph = copy.deepcopy(graph)
for i in range(N):
    for j in range(N):
        if ngraph[i][j] == 'G':
            ngraph[i][j] = 'R'

print(graph)
print(ngraph)
visited = [[False for _ in range(N)] for _ in range(N)]
D = [(1,0),(0,1),(-1,0),(0,-1)]
a, na = 0, 0

for i in range(N):
    for j in range(N):
        if visited[i][j] == False:
            dfs(i,j, graph)
            a += 1
visited = [[False for _ in range(N)] for _ in range(N)]
for i in range(N):
    for j in range(N):
        if visited[i][j] == False:
            print_graph(ngraph)
            print_graph(visited)
            dfs(i,j, ngraph)
            na += 1

print(a, na)




# 5
# RRRBB
# GGBBB
# BBBRR
# BBRRR
# RRRRR