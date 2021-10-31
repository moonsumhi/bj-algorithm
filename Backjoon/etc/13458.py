
N = int(input())
P = list(map(int, input().split()))
B, C = map(int, input().split())

ans = 0
for i in range(N):
    P[i] = max(0, P[i] - B)
ans += N

for i in range(N):
    x, r = divmod(P[i], C)
    if r:
        x += 1
    ans += x

print(ans)




# 3
# 3 4 5
# 2 2