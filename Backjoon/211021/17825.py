v = list(map(int, input().split()))

def backtracking(horses, turn, ans):
    global max_ans

    if turn == 10:
        max_ans = max(max_ans, ans)
        return

    for i in range(4):
        prev = horses[i]

        if horses[i] in intersection:
            horses[i] = board[horses[i]][1]
            cur_num = v[turn]-1
        else:
            cur_num = v[turn]

        if horses[i] + cur_num <= 21:
            horses[i] += cur_num
        else:
            for _ in range(cur_num):
                if horses[i] == 21:
                    break
                horses[i] = board[horses[i]][0]

        cnt = 0
        for horse in horses:
            if (horses[i] == horse) and (horses[i] != 21):
                cnt += 1

        if cnt >= 2:
            horses[i] = prev
            continue

        backtracking(horses, turn+1, ans+score[horses[i]])
        horses[i] = prev


# red, blue
# 21: goal
board = {i:[] for i in range(33)}
board[21].append(-1)
for i in range(21):
    board[i].append(i+1)

board[5].append(22)
for i in range(22, 27):
    board[i].append(i+1)
board[27].append(20)

board[10].append(28)
board[28].append(29)
board[29].append(25)

board[15].append(30)
for i in range(30,32):
    board[i].append(i+1)
board[32].append(25)

intersection = [5, 10, 15]
score = {}
for i in range(21):
    score[i] = 2*i

tmp = [0, 13, 16, 19, 25, 30, 35, 22, 24, 28, 27, 26]
for i in range(21, 33):
    score[i] = tmp.pop(0)

max_ans = 0
horses = [0]*4
backtracking(horses, 0, 0)
print(max_ans)














# 1 2 3 4 1 2 3 4 1 2