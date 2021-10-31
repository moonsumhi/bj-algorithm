import copy
import heapq

def update_graph(cur_node, graph):
    tmp_graph = [[] for _ in range(len(graph))]
    for i in range(1, len(graph)):
        for j in range(len(graph[i])):
            c, e = graph[i][j]
            if e == cur_node:
                tmp_graph[e].append((c, i))
                continue
            if i == cur_node:
                tmp_graph[e].append((c, i))
                continue
            tmp_graph[i].append((c, e))
    print("tmp_graph: ", tmp_graph)

    return tmp_graph


def solution(n, start, end, roads, traps):
    dp = [int(1e9)]*(n+1)
    dp[start] = 0
    traps_visited = [0]*(n+1)
    graph = [[] for _ in range(n+1)]
    for i in roads:
        s, e, c = i
        graph[s].append((c, e))

    q = []
    heapq.heappush(q, (0, start, graph))

    while q:
        cur_cost, cur, g = heapq.heappop(q)

        if cur == end:
            break

        if cur in traps:
            if traps_visited[cur] > 2:
                continue
            g = update_graph(cur, g)
            traps_visited[cur] += 1
        else:
            if cur_cost > dp[cur]:
                continue

        for n_c, nxt in g[cur]:
            if (cur_cost + n_c < dp[nxt]) or (nxt in traps):
                dp[nxt] = min(dp[nxt], cur_cost + n_c)
                print("cur, nxt, cur_cost + n_c : ", cur, nxt, cur_cost + n_c )
                heapq.heappush(q, (cur_cost + n_c, nxt, g))

    print(dp)
    return dp[end]

solution(4, 1, 4, [[1, 2, 1], [3, 2, 1], [2, 4, 1]], [2,3])