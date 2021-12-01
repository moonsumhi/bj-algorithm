import copy
from itertools import permutations
import re
from collections import deque

def cal(p, nums, not_nums):
    global answer

    for cur_op in p:
        new_nums = deque()
        new_not_nums = []
        print("nums: ", nums)
        print("not nums: ", not_nums)
        for v in not_nums:
            cur_num = nums.popleft()
            if v == cur_op:
                nums[0] = str(eval(cur_num+v+nums[0]))
            else:
                new_nums.append(cur_num)
                new_not_nums.append(v)
        while nums:
            new_nums.append(nums.popleft())
        nums = copy.deepcopy(new_nums)
        not_nums = copy.deepcopy(new_not_nums)

    tmp_answer = abs(int(nums.pop()))
    if answer < tmp_answer:
        answer = tmp_answer

    return


answer = 0
def solution(expression):
    global answer

    ps = ["+", "-", "*"]
    nums = deque(re.split('-|\+|\*', expression))
    not_nums = list(filter(lambda x: x in ps, expression))
    print(nums, not_nums)
    for p in permutations(ps, 3):
        cal(p, copy.deepcopy(nums), copy.deepcopy(not_nums))

    print(answer)
    return answer

solution("100-200*300-500+20")