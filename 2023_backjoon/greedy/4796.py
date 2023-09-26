def available_usage_days(L, P, V):
    quotient, remainder = divmod(V, P)
    return (quotient * L) + min(remainder, L)

def terminate_sign(L, P, V):
    return L == 0 and P == 0 and V == 0

if __name__ == "__main__":
    answers = []
    while True:
        L, P, V = map(int, input().split(" "))
        if terminate_sign(L, P, V):
            break
        answer = available_usage_days(L, P, V)
        answers.append(answer)

    for idx, answer in enumerate(answers):
        print(f"Case {idx+1}: {answer}")