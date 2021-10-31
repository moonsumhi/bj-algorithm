
def factorial(n):
    global f
    if n == 0 or n == 1:
        return 1

    if not f[n-1]:
        f[n-1] = factorial(n-1)
    return n*f[n-1]

T = int(input())
f = [0]*31
for _ in range(T):
    N, M = map(int, input().split())
    print(int(factorial(M)/(factorial(N)*factorial(M-N))))

# 3
# 2 2
# 1 5
# 13 29