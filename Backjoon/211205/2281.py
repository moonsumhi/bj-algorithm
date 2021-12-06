n, m = map(int, input().split())
names = [int(input()) for _ in range(n)]
d = [[-1]*(1002) for _ in range(1001)]


def go(idx, cnt):
    if idx == n:
        return 0
    print(idx, cnt)
    if d[idx][cnt] != -1:
        return d[idx][cnt]
    space = m - cnt + 1
    ans = go(idx+1, names[idx]+1) + space**2
    if cnt + names[idx] <= m:
        cur = go(idx+1, cnt+names[idx]+1)
        if cur < ans:
            ans = cur
    d[idx][cnt] = ans
    return ans

print(go(0, 0))


# 11 20
# 7
# 4
# 2
# 3
# 2
# 5
# 1
# 12
# 7
# 5
# 6