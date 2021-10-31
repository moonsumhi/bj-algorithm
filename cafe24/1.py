from collections import defaultdict

def solution(args):
    answer = []
    word_dict = defaultdict(set)

    for i in args:
        word_dict[len(i)].add(i)
    print(word_dict)
    keys = list(word_dict.keys())
    keys.sort()
    print(keys)

    for k in keys:
        tmp = list(word_dict[k])
        tmp.sort(reverse=True)
        answer.extend(tmp)
    print(answer)



    return answer


solution(["a", "aaa", "bb", "ab", "cc", "cba", "a"])