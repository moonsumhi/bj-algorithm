# 번호판에 사용할 수 있는 숫자는 0, 1, 2, ..., 8, 9이다.
# 사용할 수 있는 문자는 a, b, c, d, ..., y, z이다.
# 차량 번호판의 형식은 최대 4글자이고, c와 d로 이루어진 문자열로 나타낼 수 있다.
# c는 문자가 위치하는 자리, d는 숫자가 위치하는 자리이다.
# 같은 문자 또는 숫자가 연속해서 2번 나타나면 안 된다.

import string

def recur(i, state):
    global x, candi

    if i == len(x):
        candi.append(state)
        return

    if x[i] == "c":
        for k in list(string.ascii_lowercase):
            if i and k == state[i-1]:
                continue
            recur(i+1, state+k)
    else:
        for k in range(10):
            if i and str(k) == state[i-1]:
                continue
            recur(i+1, state+str(k))

x = input()
candi = []
recur(0, "")
print(len(candi))

