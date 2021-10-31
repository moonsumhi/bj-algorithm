

from itertools import combinations

N, M = map(int, input().split())
Board = []
for _ in range(N):
    Board.append(list(map(int, input().split())))

Chicken = []
Home = []
for i in range(N):
    for j in range(N):
        if Board[i][j] == 2:
            Chicken.append((i, j))
        if Board[i][j] == 1:
            Home.append((i,j))

ans = float('inf')
for i in list(combinations(Chicken, M)):
    city_dist = 0
    for hx, hy in Home:
        min_dist = float('inf')
        for cx, cy in i:
            min_dist = min(min_dist, abs(hx-cx) + abs(hy-cy))
        city_dist += min_dist
    ans = min(ans, city_dist)
print(ans)


# 5 2
# 0 2 0 1 0
# 1 0 1 0 0
# 0 0 0 0 0
# 2 0 0 1 1
# 2 2 0 1 2