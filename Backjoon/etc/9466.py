import sys 
sys.setrecursionlimit(100000)

def dfs(x, s):
    global p, check, checked

    if check[p[x]]:
        if p[x] in checked:
            return checked.index(p[x])
        else:
            return len(checked)
    else:
        check[p[x]] = True
        checked.append(p[x])
        return dfs(p[x], s)

T = int(input())
for _ in range(T):
    N = int(input())
    p = [0] + list(map(int, input().split()))
    check = [False]*(N+1)
    for i in range(1, N+1):
        if not check[i]:
            checked = []
            s_index = dfs(i, i)
            for c in range(s_index):
                check[checked[c]] = False

    print(N-sum(check))

# 2
# 7
# 3 1 3 7 3 4 6
# 8
# 1 2 3 4 5 6 7 8