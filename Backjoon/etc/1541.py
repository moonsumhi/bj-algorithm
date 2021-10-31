import re
from collections import deque

exp = "55-50+40-20+10"

# operator = deque(re.split('[\-\+]', exp))
# operand = re.split('[0-9*]', exp)
# operand = deque(filter(lambda a: a != '', operand))

if "-" in exp:
    plus_exp = exp.split("-")
    print(plus_exp)
    for i in range(len(plus_exp)):
        num = re.split('[\+]', plus_exp[i])
        tmp = str(int(num[0]))
        for j in num[1:]:
            tmp += "+"
            tmp += str(int(j))
        plus_exp[i] = str(eval(tmp))

    answer = plus_exp[0]
    for i in plus_exp[1:]:
        answer = str(eval(answer+"-"+i))
else:
    print(eval(exp))
print(answer)


