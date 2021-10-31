from collections import Counter

def solution(lottos, win_nums):
    answer = []
    zero = Counter(lottos)[0]
    hit_cnt = 0
    for i in lottos:
        if not i:
            continue
        if i in win_nums:
            hit_cnt += 1

    best = hit_cnt + zero
    worst = hit_cnt

    order = {6: 1, 5: 2, 4: 3, 3: 4, 2: 5, 1: 6, 0: 6}
    answer = [order[best], order[worst]]
    print(answer)

    return answer

solution([0, 0, 0, 0, 0, 0], [38, 19, 20, 40, 15, 25])