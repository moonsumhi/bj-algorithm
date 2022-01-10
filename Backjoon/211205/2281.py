n, m = map(int, input().split())
names = [int(input()) for i in range(n)]
d = [[-1]*1001 for _ in range(n+1)]

def go(i, cnt):
    if i == n:
        return 0
    if d[i][cnt] != -1:
        return d[i][cnt]
    space = m-cnt+1
    ans = go(i+1, names[i]+1) + space**2
    if cnt+names[i] <= m:
        ans = min(ans, go(i+1, cnt+names[i]+1))
    d[i][cnt] = ans

    return ans

print(go(1, names[0]+1))

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