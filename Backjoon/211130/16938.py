from itertools import combinations

n, l, r, x = map(int, input().split())
a = list(map(int, input().split()))

ans = 0
for cnt in range(2, n+1):
    for i in combinations(a, cnt):
        temp = sum(i)
        if (l <= temp <= r) and (max(i)-min(i) >= x):
            ans += 1
print(ans)


# 3 5 6 1
# 1 2 3