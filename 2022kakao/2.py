import math

def de2q(n, q):
    rev_base = ''

    while n > 0:
        n, mod = divmod(n, q)
        rev_base += str(mod)

    return rev_base[::-1]


def is_prime_number(x):
    if x == 1:
        return False

    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


def solution(n, k):
    answer = 0
    num = de2q(n, k)
    num_list = num.split('0')
    print(num_list)
    for i in num_list:
        if not i:
            continue
        if is_prime_number(int(i)):
            answer += 1
    print(answer)

    return answer

solution(110011, 10)