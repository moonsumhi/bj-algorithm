n, l, r, x = map(int, input().split())
a = list(map(int, input().split()))
c = [False] * (n+1)
def go(index):

    if index == n:
        cnt = 0
        tot = 0
        hard = -1
        easy = -1
        for i in range(n):
            if c[i] == False:
                continue
            tot += a[i]
            cnt += 1
            if hard == -1 or hard < a[i]:
                hard = a[i]
            if easy == -1 or easy > a[i]:
                easy = a[i]
        if cnt >= 2 and l <= tot <= r and hard-easy >= x:
            return 1
        else:
            return 0

    c[index] = True
    cnt1 = go(index+1)
    c[index] = False
    cnt2 = go(index+1)

    return cnt1+cnt2
print(go(0))