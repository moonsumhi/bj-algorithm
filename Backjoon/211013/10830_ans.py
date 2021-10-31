import sys

def prod(a, b):
    n = len(a)
    c = [[0 for __ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                c[i][j] += a[i][k] * b[k][j]
    remainder(c)
    return c

def remainder(A):
    n = len(A)
    for i in range(n):
        for j in range(n):
            A[i][j] %= 1000

def dnq(A, B):
    if B == 1: return A
    x = dnq(A, B//2)
    if B % 2: return prod(prod(x, x), A)
    else: return prod(x, x)

N, B = map(int, sys.stdin.readline().split())
A = []
for i in range(N):
    A.append(list(map(int, sys.stdin.readline().split())))
remainder(A)
print("\n".join(map(lambda x: " ".join(map(str, x)), dnq(A, B))))