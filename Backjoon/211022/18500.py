from collections import deque

R, C = map(int, input().split())
cave = []
for _ in range(R):
    cave.append(list(input()))
N = int(input())
heights = list(map(int, input().split()))

def update_cave(r, turn):
    global cave

    cur_height = cave[r]
    if turn == 1:
        for i in range(C):
            if cur_height[i] == 'x':
                cur_height[i] = '.'
                break
    else:
        for i in range(C-1, -1, -1):
            if cur_height[i] == 'x':
                cur_height[i] = '.'
                break
    cave[r] = cur_height

    # check if it is levitating
    visited = [[False for __ in range(C)] for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if (cave[i][j] == 'x') and (not visited[i][j]):
                visited[i][j] = True
                mxy = isLevitating(cave, i, j, visited)
                if mxy != 1:
                    cave = falling(cave, mxy[1], max(mxy[0]))
                    return

    return -1

def print_graph(g):
    print("=======")
    for i in g:
        print(i)

def falling(c, my, mx):
    print("before: ")
    print_graph(c)

    print(my)
    cave_zip = list(map(list, zip(*c)))
    print("zipped: ")
    print_graph(cave_zip)

    flag = 0
    while True:
        for i in my:
            s = mx
            while cave_zip[i][s] != '.':
                s -= 1
            cave_zip[i].pop(s)
            cave_zip[i].insert(0, '.')

            if cave_zip[i][s] == 'x':
                flag = 1

        if flag:
            break

    cave = list(map(list, zip(*cave_zip)))
    print("after: ")
    print_graph(cave)

    return cave


def isLevitating(c, x, y, visited):
    q = deque()
    q.append([x, y])

    mx = {x}
    my = {y}
    flag = 0
    while q:
        cx, cy = q.popleft()

        for i, j in [(1,0), (0,1), (-1,0), (0,-1)]:
            nx, ny = cx+i, cy+j
            if nx < 0 or ny < 0 or nx >= R or ny >= C:
                continue
            if not visited[nx][ny]:
                visited[nx][ny] = True
                if c[nx][ny] == 'x':
                    q.append([nx, ny])
                    mx.add(nx)
                    my.add(ny)
                    if nx == R-1:
                        flag = 1

    if flag:
        return 1

    return [mx, my]

# left : 1
# right : -1
turn = 1
for i in heights:
    r = R-i
    update_cave(r, turn)
    turn *= -1

for i in cave:
    print(''.join(i))

# 8 8
# ........
# ........
# ...x.xx.
# ...xxx..
# ..xxx...
# ..x.xxx.
# ..x...x.
# .xxx..x.
# 5
# 6 6 4 3 1

# 5 5
# xxxxx
# x....
# xxxxx
# x....
# x....
# 10
# 1 2 3 4 5 1 2 3 4 5

# .....
# .....
# .....
# .xxxx
# xxxx.