

N = int(input())
ele = list(map(int, input().split()))
dp = [{ele[i]} for i in range(N)]

for i in range(1, N):
    for j in range(i):
        if ele[i] > ele[j]:
            if len(dp[i]) < len(dp[j])+1:
                dp[i] = dp[j].union({ele[i]})

print(dp)

max_v = 0
ans = {}
for i in dp:
    if len(i) > max_v:
        max_v = len(i)
        ans = i
ans = list(ans)
ans.sort()
print(max_v)
print(*ans)
# 6
# 10 20 10 30 20 50

# 7
# 1 6 2 4 5 3 7