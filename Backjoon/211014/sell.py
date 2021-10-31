def solution(enroll, referral, seller, amount):
    enroll_dict = {i:0 for i in enroll}
    parents = {}
    for i in range(len(enroll)):
        parents[enroll[i]] = referral[i]

    for i in range(len(seller)):
        cur_person = seller[i]
        profit = amount[i] * 100
        while cur_person != "-":
            if profit < 10:
                enroll_dict[cur_person] += profit
                break
            fee = int(profit * 0.1)
            profit = profit - fee
            enroll_dict[cur_person] += int(profit)
            cur_person = parents[cur_person]
            profit = fee

    answer = list(enroll_dict.values())

    return answer

solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"], ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"], ["young", "john", "tod", "emily", "mary"], [12, 4, 2, 5, 10])