from collections import deque,defaultdict
import math

def str2time(t):
    h, m = t.split(":")
    return int(h)*60+int(m)


def solution(fees, records):
    answer = []
    id_dict = defaultdict(list)
    used_time = defaultdict(int)

    for i in records:
        t, id, in_out = i.split()
        min_t = str2time(t)

        # in & out
        if not id_dict[id]:
            id_dict[id].append(min_t)
        else:
            used_time[id] += min_t - id_dict[id].pop()


    for idx, v in id_dict.items():
        if id_dict[idx]:
            used_time[idx] += str2time("23:59") - id_dict[idx].pop()
    print(used_time)

    answer = {i:0 for i in used_time.keys()}
    for id, v in used_time.items():
        if used_time[id] > fees[0]:
            used_time[id] -= fees[0]
            remained = math.ceil((used_time[id]/fees[2]))*fees[3]
            answer[id] = fees[1] + remained
        else:
            answer[id] = fees[1]

    print(answer)
    answer = sorted(answer.items())
    print(list(list(zip(*answer))[1]))

    return list(list(zip(*answer))[1])

solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"])