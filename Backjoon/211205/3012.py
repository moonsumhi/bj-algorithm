# 10
# (?([?)]?}?

n = int(input())
s = input()
d = [[-1]*200 for _ in range(200)]
open = ['(', '{', '[']
close = [')', '}', ']']
mod = 100000

def go(i, j):
    if i > j:
        return 1
    ans = d[i][j]
    if ans != -1:
        return ans
    ans = 0
    for k in range(i+1, j, 2):
        for l in range(3):
            if s[i] == open[l] or s[i] == '?':
                if s[k] == close[l] or s[k] == '?':
                    temp = go(i+1, k-1)*go(k+1, j)
                    ans += temp
                    if ans >= mod:
                        ans = mod + ans%mod

    d[i][j] = ans
    return ans

ans = go(0, n-1)
if ans >= mod:
    print(str(ans%mod)[-5:])
else:
    print(ans)




