import sys
sys.setrecursionlimit(10000)


def check(a):
    global DP, ANS

    for k in graph[a]:
        if DP[k]:
            if DP[k] == DP[a]:
                ANS = "NO"
                return
            else:
                continue
        else:
            DP[k] = DP[a] * -1
            check(k)

    return


DP = []
ANS = "YES"
t = int(input())
for i in range(t):
    ANS = "YES"
    v_num, e_num = map(int, input().split())
    graph = [[] for _ in range(v_num+1)]
    for j in range(e_num):
        s, t = map(int, input().split())
        graph[s].append(t)
        graph[t].append(s)
    print(graph)

    DP = [0] * (v_num + 1)
    for k in range(1, v_num+1):
        if DP[k] == 0:
            DP[k] = 1
            check(k)
        if ANS == "NO":
            break

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

