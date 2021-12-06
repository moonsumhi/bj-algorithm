s = input()
limit = [0, 0, 0]
n = len(s)
for ch in s:
    limit[ord(ch)-ord('A')] += 1
d = [[[[[-1]*3 for l in range(3)] for k in range(51)] for j in range(51)] for i in range(51)]

def go(a, b, c, p1, p2):
    if a+b+c==n:
        d[a][b][c][p1][p2] = 1
        return d[a][b][c][p1][p2]
    if d[a][b][c][p1][p2] != -1:
        return d[a][b][c][p1][p2]
    if a+1 <= limit[0] and go(a+1, b, c, 0, p1):
        d[a][b][c][p1][p2] = 1
        return d[a][b][c][p1][p2]
    if b+1 <= limit[1] and p1 != 1:
        if go(a, b+1, c, 1, p1):
            d[a][b][c][p1][p2] = 1
            return d[a][b][c][p1][p2]
    if c+1 <= limit[2] and p1 != 2 and p2 != 2:
        if go(a, b, c+1, 2, p1):
            d[a][b][c][p1][p2] = 1
            return d[a][b][c][p1][p2]
    d[a][b][c][p1][p2] = 0
    return d[a][b][c][p1][p2]

def back(a, b, c, p1, p2):
    if a+b+c==n:
        return ''
    if a+1 <= limit[0] and go(a+1, b, c, 0, p1) == 1:
        return 'A' + back(a+1, b, c, 0, p1)
    if b+1 <= limit[1] and p1 != 1:
        if go(a, b+1, c, 1, p1):
            return 'B' + back(a, b+1, c, 1, p1)
    if c+1 <= limit[2] and p1 != 2 and p2 != 2:
        if go(a, b, c+1, 2, p1):
            return 'C' + back(a, b, c+1, 2, p1)

ans = go(0, 0, 0, 0, 0)
if ans == 0:
    print('-1')
else:
    print(back(0, 0, 0, 0, 0))
