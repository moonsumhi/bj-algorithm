def dfs(n, check, d, idx, cnt, ans):
    if idx >= len(d):
        return ans

    if check == [0]*n:
        ans = min(ans, idx)
        return ans
    else:
        for i in range(n):
            tmp = []
            partial_c = []
            if i + d[idx] > n:
                partial_c = [x for x in range(i, n)] + [x for x in range(0, i+d[idx]-n)]
            else:
                partial_c = [x for x in range(i, i + d[idx])]
            # print("idx, d[idx]: ", idx, d[idx])
            # print("partial_c: ", partial_c)

            for j in partial_c:
                if check[j] == 1:
                    check[j] = 0
                    tmp.append(j)
            # print("check : ", check)
            ans = dfs(n, check, d, idx+1, cnt+1, ans)
            for k in tmp:
                check[k] = 1

            # back
            if i - d[idx] < 0:
                partial_c = [x for x in range(i, 0, -1)] + [x for x in range(-1,i-d[idx]-1,-1)]
            else:
                partial_c = [x for x in range(i, i - d[idx], -1)]

            for j in partial_c:
                if check[j] == 1:
                    check[j] = 0
                    tmp.append(j)
            # print("check : ", check)
            ans = dfs(n, check, d, idx+1, cnt+1, ans)
            for k in tmp:
                check[k] = 1

    return ans


def solution(n, weak, dist):
    answer = int(1e9)
    check = [0]*n
    for i in weak:
        check[i] = 1
    answer = dfs(n, check, dist[::-1], 0, 0, answer)
    if answer == int(1e9):
        answer = -1
    return answer

solution(12, [1, 5, 6, 10], [1, 2, 3, 4])