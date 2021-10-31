from itertools import permutations
import re
import copy

def solution(expression):
    answer = 0
    perm = list(permutations(['*', '-', '+'], 3))

    expression = re.split('([-+*])', expression)

    for o in perm:
        order_list = list(o)
        tmp_expression = expression[:]
        for i in order_list:
            while i in tmp_expression:
                idx = tmp_expression.index(i)
                tmp_expression[idx-1] = str(eval(tmp_expression[idx-1] + i + tmp_expression[idx+1]))
                del tmp_expression[idx:idx+2]
                print(tmp_expression)
        answer = max(answer, abs(int(tmp_expression[0])))

    print(answer)



    return answer

solution("50*6-3*2")