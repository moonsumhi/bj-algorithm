
def solution(n, s, a, b, fares):
    costs = [[int(1e9)]*(n+1) for _ in range(n+1)]

    for i in fares:
        x, y, c = i
        costs[x][y] = c
        costs[y][x] = c

    for i in range(1, n+1):
        costs[i][i] = 0

    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                costs[i][j] = min(costs[i][j], costs[i][k]+costs[k][j])

    answer = costs[s][a] + costs[s][b]
    for i in range(1, n+1):
        answer = min(answer, costs[s][i] + costs[i][a] + costs[i][b])

    print(answer)

    return

solution(6,4,5,6, [[2,6,6], [6,3,7], [4,6,7], [6,5,11], [2,5,12], [5,3,20], [2,4,8], [4,3,9]])