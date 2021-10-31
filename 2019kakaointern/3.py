from itertools import permutations

def check_id(id, banned_id):
    N = len(id)

    if N != len(banned_id):
        return False

    for i in range(N):
        if banned_id[i] == '*':
            continue
        else:
            if id[i] != banned_id[i]:
                return False

    return True


def check(ids, banned_ids):
    for i in range(len(ids)):
        if check_id(ids[i], banned_ids[i]):
            continue
        else:
            return False
    return True


def solution(user_id, banned_id):
    answer = []
    for i in permutations(user_id, len(banned_id)):
        if check(i, banned_id):
            answer.append(i)
    s_answer = []
    for i in answer:
        tmp = set(i)
        if tmp not in s_answer:
            s_answer.append(tmp)

    return len(s_answer)

# solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"])
solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"])