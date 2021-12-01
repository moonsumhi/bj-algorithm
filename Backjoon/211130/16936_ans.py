n = int(input())
a = list(map(int, input().split()))
for i in range(a):
    num = a[i]
    cnt = 0
    while num%3 == 0:
        num = num //3
        cnt += 1
    a[i] = (-cnt, a[i])
a.sort()
ans = [x[1] for x in a]
print(*ans, sep='')