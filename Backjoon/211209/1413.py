import sys, math

n, m = map(int, sys.stdin.readline().split())
d = [[0] * 21 for _ in range(21)]

d[1][1] = 1

for i in range(2, n+1):
    for j in range(1, i+1):
        d[i][j] = d[i-1][j-1] + (i-1)*d[i-1][j]

bunza = 0
for i in range(1, m+1):
    bunza += d[n][i]

bunmo = 1
for i in range(1, n+1):
    bunmo *= i

print('%d/%d'%(bunza//math.gcd(bunza, bunmo), bunmo//math.gcd(bunza, bunmo)))