def solution(id_list, report, k):
    answer = []
    ids = {i:set() for i in id_list}
    s_id = {i:0 for i in id_list}
    for i in report:
        a, b = i.split()
        ids[a].add(b)

    print(ids)

    for idx, v in ids.items():
        for i in v:
            s_id[i] += 1

    print(s_id)



    banned = []
    for idx, v in s_id.items():
        if v >= k:
            banned.append(idx)
    print(banned)

    for idx, v in ids.items():
        nums = 0
        for i in banned:
            if i in v:
                nums += 1
        answer.append(nums)
    print(answer)

    return answer

solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2)
