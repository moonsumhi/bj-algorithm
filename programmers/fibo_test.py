

def fibo(n):
    global memo

    if not memo[n-1]:
        memo[n-1] = fibo(n-1)

    if not memo[n-2]:
        memo[n-2] = fibo(n-2)

    return memo[n-1]+memo[n-2]

memo = [0] * 100
memo[1], memo[2] = 1, 1
fibo(43)
print(memo)

