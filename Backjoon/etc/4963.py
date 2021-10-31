def print_island(g):
    print("==========")
    for i in g:
        print(i)

def dfs(x, y):
    global w, h, island

    island[x][y] = 0

    for i, j in D:
        n_x, n_y = x+i, y+j

        if n_x < 0 or n_y < 0 or n_x >= h or n_y >= w:
            continue
        if island[n_x][n_y] == 1:
            dfs(n_x, n_y)

while True:
    w, h = map(int, input().split())
    if not w:
        break
    island = []
    for _ in range(h):
        island.append(list(map(int, input().split())))
    print_island(island)
    D = [(1,0),(0,1),(-1,0),(0,-1),(-1,-1),(1,1),(1,-1),(-1,1)]
    cnt = 0
    for i in range(h):
        for j in range(w):
            if island[i][j] == 1:
                dfs(i,j)
                cnt += 1
    print(cnt)


# 1 1
# 0
# 2 2
# 0 1
# 1 0
# 3 2
# 1 1 1
# 1 1 1
# 5 4
# 1 0 1 0 0
# 1 0 0 0 0
# 1 0 1 0 1
# 1 0 0 1 0
# 5 4
# 1 1 1 0 1
# 1 0 1 0 1
# 1 0 1 0 1
# 1 0 1 1 1
# 5 5
# 1 0 1 0 1
# 0 0 0 0 0
# 1 0 1 0 1
# 0 0 0 0 0
# 1 0 1 0 1
# 0 0