from collections import deque

def bfs():
    global ANS

    while Q:
        cur = Q.popleft()

        for k in graph[cur]:
            if dp[k] == 0:
                dp[k] = dp[cur]*-1
                Q.append(k)
            else:
                if dp[k] == dp[cur]:
                    ANS = "NO"
                    while Q:
                        Q.popleft()
                    return
    return



ANS = "YES"
t = int(input())
Q = deque()
for i in range(t):
    ANS = "YES"
    v_num, e_num = map(int, input().split())
    graph = [[] for _ in range(v_num+1)]
    for j in range(e_num):
        s, t = map(int, input().split())
        graph[s].append(t)
        graph[t].append(s)
    print(graph)

    dp = [0] * (v_num+1)

    for k in range(1, v_num+1):
        if dp[k] == 0:
            dp[k] = 1
            Q.append(k)
            bfs()

    print(ANS)



# 2
# 3 2
# 1 3
# 2 3
# 4 4
# 1 2
# 2 3
# 3 4
# 4 2

