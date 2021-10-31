n = int(input())
s = []
for i in range(n):
    first, second = map(int, input().split())
    s.append([first, second])
s = sorted(s, key=lambda a: a[0])
s = sorted(s, key=lambda a: a[1])
last = 0
cnt = 0
print(s)
for i, j in s:
    if i >= last:
        cnt += 1
        last = j
print(cnt)


# 11
# 1 4
# 3 5
# 0 6
# 5 7
# 3 8
# 5 9
# 6 10
# 8 11
# 8 12
# 2 13
# 12 14