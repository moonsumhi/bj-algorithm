import copy


def solution(leave, day, holidays):
    answer = -1
    days = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
    new_days = days[days.index(day):] + days[:days.index(day)]

    cal = {}
    for i in range(1, 31):
        cal[i] = new_days[(i%7)-1]
    print(cal)

    result = 0
    for i in range(1, 31):
        tmp_leave = leave
        result = 0
        if (cal[i] in ["SAT", "SUN"]) or (i in holidays):
            result += 1
        else:
            tmp_leave -= 1
            result += 1

        for j in range(i+1, 31):

            if j in holidays:
                result += 1
                answer = max(answer, result)
                continue
            if cal[j] in ["SAT", "SUN"]:
                result += 1
                answer = max(answer, result)
                continue

            if not tmp_leave:
                answer = max(answer, result)
                break

            tmp_leave -= 1
            result += 1

    print(answer)

    return answer

solution(4, "FRI", 	[6, 21, 23, 27, 28])
# solution(3, "SUN", [2,6,17,29])