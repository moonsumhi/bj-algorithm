def dfs(cur_sum, cur_cnt, target, t_cnt, numbers):
    global answer

    if (cur_sum == target) and (cur_cnt == t_cnt):
        answer += 1
        return

    if cur_cnt > t_cnt-1:
        return

    dfs(cur_sum + numbers[cur_cnt], cur_cnt + 1, target, t_cnt, numbers)
    dfs(cur_sum - numbers[cur_cnt], cur_cnt + 1, target, t_cnt, numbers)

    return


answer = 0

def solution(numbers, target):
    global answer

    t_cnt = len(numbers)
    dfs(0, 0, target, t_cnt, numbers)

    return answer

solution([1, 1, 1, 1, 1], 3)